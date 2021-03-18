import os
from flask import Flask

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

    @app.route('/actors/<int:id>', methods=['PATCH'])
    def post_actor():
        if request.method == "PATCH":
            body = request.get_json()

            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)
            
            actor = Actor.query.filter_by(id=id).one_or_none()
            
            actor.name = name
            actor.age = age
            actor.gender = gender

            actor.update()

            return jsonify({
                'success': True,
                'updated_actor': id,
                'total_actors': len(Actor.query.all())
            })
    return app

app = create_app()

if __name__ == '__main__':
    app.run()