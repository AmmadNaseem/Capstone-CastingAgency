# from models import *
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ====================DB STRING==================
DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '134256')
DB_NAME = os.getenv('DB_NAME', 'capstone')
database_path = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)


db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()

      


# ===============MODELS==============
class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=True)

    def __repr__(self):
        return f"<Actor id={self.id} name={self.name} gender={self.gender} age={self.age}>"
    
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            "movie_id": self.movie_id
        }

# ==================MOVIES MODELS===========
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    actors = db.relationship('Actor', backref="movies", lazy=True)

    def __repr__(self):
        return f"<Movie id={self.id} title={self.title} release_date={self.release_date}>  Actors={self.movies}"

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': list(map(lambda actor: actor.format(), self.actors))
        }

