import os
from flask import Flask, jsonify

from flask_cors import CORS
from database.models import setup_db, Actor, Movie
from auth.auth import AuthError, requires_auth
def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)

    CORS(app)


    @app.route('/')
    def get_greeting():
        return "Hello world!"

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/actors', methods=['GET'])
    def get_all_actors():
        actors = Actor.query.all()
        actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors
        }), 200
    return app

app = create_app()

if __name__ == '__main__':
    app.run()