import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os


database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''


actor_movie = db.Table(
    'actor_movie',
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True),
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True)
)
class Movie(db.Model):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)

    cast = db.relationship('Actor', secondary=actor_movie, backref=db.backref('movies', lazy=True))

    def __init__(self, title, release_year, duration):
        self.title = title
        self.release_year = release_year
        self.duration = duration

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return f'<{self.id} - {self.title} - {self.release_year}>'

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'duration': self.duration
        }



class Actor(db.Model):  
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return f'<{self.id} - {self.name}>'

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'created_at': self.created_at
        }