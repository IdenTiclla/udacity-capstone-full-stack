import os
from flask import (
    Flask,
    jsonify,
    request,
    abort
)

from flask_cors import CORS
from database.models import setup_db, Actor, Movie
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)

    CORS(app)

    @app.route('/')
    def get_greeting():
        return jsonify({
            'success': True,
            'message': 'Healthy!!'
        })

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/actors', methods=['GET'])
    @requires_auth("get:actors")
    def get_all_actors(payload):
        actors = Actor.query.order_by(Actor.id).all()
        actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors
        }), 200

    @app.route('/actors/<int:id>', methods=['GET'])
    @requires_auth('get:actors-info')
    def get_specific_actor(payload, id):
        actor = Actor.query.filter_by(id=id).one_or_none()
        if actor is None:
            abort(404)
        return jsonify({
            'success': True,
            'actor': actor.format()
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actor(payload):
        if request.method == "POST":
            body = request.get_json()
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()

            return jsonify({
                'success': True,
                'created_actor': actor.name,
                'total_actors': len(Actor.query.all())
            })

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor(payload, id):
        if request.method == "PATCH":
            body = request.get_json()

            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)

            actor = Actor.query.filter_by(id=id).one_or_none()

            if actor is None:
                abort(404)

            actor.name = name
            actor.age = age
            actor.gender = gender
            actor.update()

            return jsonify({
                'success': True,
                'patched_actor': id,
                'total_actors': len(Actor.query.all())
            })

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        actor = Actor.query.filter_by(id=id).one_or_none()

        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            'success': True,
            'deleted': id,
            'total_actors': len(Actor.query.all())
        }), 200

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_all_movies(payload):
        movies = Movie.query.order_by(Movie.id).all()
        movies = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': movies
        }), 200

    @app.route('/movies/<int:id>', methods=['GET'])
    @requires_auth('get:movies-info')
    def get_specific_movie(payload, id):
        movie = Movie.query.filter_by(id=id).one_or_none()
        if movie is None:
            abort(404)

        return jsonify({
            'success': True,
            'movie': movie.format()
        })

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        movie = Movie.query.filter_by(id=id).one_or_none()

        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
            'success': True,
            'deleted': id,
            'total_movies': len(Movie.query.all())
        }), 200

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movie(payload):
        if request.method == "POST":
            body = request.get_json()

            title = body.get('title', None)
            release_year = body.get('release_year', None)
            duration = body.get('duration', None)

            movie = Movie(
                title=title,
                release_year=release_year,
                duration=duration)
            movie.insert()

            return jsonify({
                'success': True,
                'created_movie': movie.id,
                'total_movies': len(Movie.query.all())
            }), 200

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie(payload, id):
        if request.method == "PATCH":
            movie = Movie.query.filter_by(id=id).one_or_none()
            if movie is None:
                abort(404)
            body = request.get_json()
            title = body.get('title', None)
            release_year = body.get('release_year', None)
            duration = body.get('duration', None)

            movie.title = title
            movie.release_year = release_year
            movie.duration = duration

            movie.update()

            return jsonify({
                'success': True,
                'updated_movie': id,
                'total_movies': len(Movie.query.all())
            })

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 422

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
