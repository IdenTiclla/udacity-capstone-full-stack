import os
from flask import Flask, jsonify, request, abort

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

    @app.route('/actors', methods=['POST'])
    def post_actor():
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

    @app.route('/actors', methods=['GET'])
    def get_all_actors():
        actors = Actor.query.all()
        actors = [actor.format() for actor in actors]

        return jsonify({
            'success': True,
            'actors': actors
        }), 200

    @app.route('/actors/<int:id>', methods=['GET'])
    def get_specific_actor(id):
        actor = Actor.query.filter_by(id=id).one_or_none()
        if actor is None:
            abort(404)
        return jsonify({
            'success': True,
            'actor': actor.format()
        })

    @app.route('/actors/<int:id>', methods=['DELETE'])
    def delete_actor(id):
        actor = Actor.query.filter_by(id=id).one_or_none()
        
        if actor is None:
            abort(404)

        actor.delete()
        
        return jsonify({
            'success': True,
            'deleted': id,
            'total_actors': len(Actor.query.all())
        }), 200

    return app

app = create_app()

if __name__ == '__main__':
    app.run()