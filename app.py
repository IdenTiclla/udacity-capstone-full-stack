import os
from flask import Flask, abort, jsonify

from flask_cors import CORS
from database.models import setup_db, Actor
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