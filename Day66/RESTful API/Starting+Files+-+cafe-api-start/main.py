import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import load_only
API_KEY = 'SBDKVJHFVKWJGDUBHWE1233452'
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    cafe = random.choice(cafes)
    return jsonify(cafe={
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price,
    })

@app.route('/all')
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        cafe_data = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        cafe_list.append(cafe_data)
    return jsonify(cafe=cafe_list)


@app.route('/search')
def get_search_cafe():
    loc = request.args.get('loc')
    searched_cafe = Cafe.query.filter_by(location=loc).first()
    if searched_cafe:
        return jsonify(cafe={
            "id": searched_cafe.id,
            "name": searched_cafe.name,
            "map_url": searched_cafe.map_url,
            "img_url": searched_cafe.img_url,
            "location": searched_cafe.location,
            "seats": searched_cafe.seats,
            "has_toilet": searched_cafe.has_toilet,
            "has_wifi": searched_cafe.has_wifi,
            "has_sockets": searched_cafe.has_sockets,
            "can_take_calls": searched_cafe.can_take_calls,
            "coffee_price": searched_cafe.coffee_price,
        })
    else:
        return jsonify(error={
            "Not Found": "We don't have a cafe at that location."
        })


## HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
            "Success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=["GET", "PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={
            "Success": "Successfully updated the new cafe."}), 200
    else:
        return jsonify(response={
            "Not Found": "Sorry cafe with that id not found in database."}), 404


## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get("api-key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        if api_key == API_KEY:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={
                "Success": "Successfully updated the new cafe."}), 200
        else:
            return jsonify(response={
                "error": "Sorry, that's not allowed. Make sure you have the correct api-key."}), 200
    else:
        return jsonify(response={
            "Not Found": "Sorry cafe with that id not found in database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
