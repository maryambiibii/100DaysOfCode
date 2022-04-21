from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy
app = Flask(__name__)

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create Table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.FLOAT, nullable=False)


#db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Create Record
        new_book = Books(
            title=request.form.get("name"),
            author=request.form.get("author"),
            rating=request.form.get("rating"))
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit<int:id>", methods=['GET', 'POST'])
def edit_rating(id):
    if request.method == 'POST':
        book_to_update = Books.query.get(id)
        book_to_update.rating = request.form.get("new_rating")
        db.session.commit()
        return redirect(url_for('home'))
    selected_book = Books.query.filter_by(id=id).first()
    return render_template('EditRating.html', book=selected_book)


@app.route("/delete<int:id>", methods=['GET', 'POST'])
def delete(id):
    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

