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

    return app

app = create_app()

if __name__ == '__main__':
    app.run()