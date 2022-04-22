from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from sqlalchemy import desc

import requests

API_KEY = 'your_tmdb_key'
URL = 'https://api.themoviedb.org/3/search/movie'

app = Flask(__name__)

# 1.Create Database
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


# 2.Create Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()
"""
# 3.Create Record
new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
db.session.add(new_movie)
db.session.commit()
"""


class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your Rating Out of 10 e.g. 6.8', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddMovie(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    add_movie = SubmitField(label='Add Movie')


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating.asc()).all()
    ranking = len(all_movies)
    for movies in all_movies:
        movies.ranking = ranking
        db.session.commit()
        ranking -= 1
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    if form.validate_on_submit():
        id = request.args.get('id')
        movie_to_update = Movie.query.get(id)
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    id = request.args.get('id')
    book_to_delete = Movie.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        params = {
            'api_key': API_KEY,
            'query': form.movie_title.data,
        }
        response = requests.get(URL, params=params)
        data = response.json()
        all_matched_movies = data['results']
        return render_template('select.html', movies=all_matched_movies)
    return render_template('add.html', form=form)


@app.route('/get_movie_details', methods=['GET', 'POST'])
def get_movie_details():
    id = request.args.get('id')

    # Make API Request
    M_URL = f'https://api.themoviedb.org/3/movie/{id}'
    params = {
        'api_key': API_KEY,
    }
    response = requests.get(M_URL, params=params)
    data = response.json()
    print(data)

    # Create Record
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'],
        description=data['overview'],
        img_url=f'http://image.tmdb.org/t/p/w500/{data["poster_path"]}'
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
