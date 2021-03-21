import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database.models import setup_db, Actor, Movie


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.CASTING_ASSISTANT = os.environ['CASTING_ASSISTANT']
        self.CASTING_DIRECTOR = os.environ['CASTING_DIRECTOR']
        self.EXECUTIVE_PRODUCER = os.environ['EXECUTIVE_PRODUCER']

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.new_actor = {
            "name": "William",
            "age": 32,
            "gender": "male"
        }

        self.new_movie = {
            "title": "Dr Strange",
            "duration": 3,
            "release_year": 2016
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            self.db.create_all()

    def tearDown(self):
        pass

    def test_health(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['message'], 'Healthy!!')

    def test_get_actors_without_token(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, 401)

    def test_get_actors_with_valid_token(self):
        res = self.client().get(
            '/actors',
            headers={
                "Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"})
        self.assertEqual(res.status_code, 200)

    def test_get_specific_actor_without_token(self):
        res = self.client().get('/actors/8')
        self.assertEqual(res.status_code, 401)

    def test_get_specific_actor_with_valid_token(self):
        res = self.client().get(
            '/actors/8',
            headers={
                "Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"})
        self.assertEqual(res.status_code, 200)

    def test_create_actor_without_token(self):
        res = self.client().post('/actors', json=self.new_actor)
        self.assertEqual(res.status_code, 401)

    def test_create_actor_with_valid_token(self):
        res = self.client().post(
            '/actors',
            headers={
                "Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"},
            json=self.new_actor)
        self.assertEqual(res.status_code, 200)

    def test_patch_actor_without_token(self):
        res = self.client().patch('/actors/8', json=self.new_actor)
        self.assertEqual(res.status_code, 401)

    def test_patch_actor_with_valid_token(self):
        res = self.client().patch(
            '/actors/8',
            headers={
                "Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"},
            json=self.new_actor)
        self.assertEqual(res.status_code, 200)

    def test_delete_actor_without_token(self):
        res = self.client().delete('/actors/10')
        self.assertEqual(res.status_code, 401)

    def test_delete_actor_with_valid_token(self):
        res = self.client().delete('/actors/10',
                                   headers={"Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"})
        self.assertEqual(res.status_code, 200)
    # TESTS FOR MOVIES

    def test_get_movies_without_token(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, 401)

    def test_get_movies_with_valid_token(self):
        res = self.client().get(
            '/movies',
            headers={
                "Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"})
        self.assertEqual(res.status_code, 200)

    def test_get_specific_movie_without_token(self):
        res = self.client().get('/movies/6')
        self.assertEqual(res.status_code, 401)

    def test_get_specific_movie_with_valid_token(self):
        res = self.client().get(
            '/movies/6',
            headers={
                "Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"})
        self.assertEqual(res.status_code, 200)

    def test_create_movie_without_token(self):
        res = self.client().post('/movies', json=self.new_movie)
        self.assertEqual(res.status_code, 401)

    def test_create_movie_with_valid_token(self):
        res = self.client().post(
            '/movies',
            headers={
                "Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"},
            json=self.new_movie)
        self.assertEqual(res.status_code, 200)

    def test_patch_movie_without_token(self):
        res = self.client().patch('/movies/6', json=self.new_movie)
        self.assertEqual(res.status_code, 401)

    def test_patch_movie_with_valid_token(self):
        res = self.client().patch(
            '/movies/6',
            headers={
                "Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"},
            json=self.new_movie)
        self.assertEqual(res.status_code, 200)

    def test_delete_movie_without_token(self):
        res = self.client().delete('/movies/8')
        self.assertEqual(res.status_code, 401)

    def test_delete_movie_with_valid_token(self):
        res = self.client().delete('/movies/8',
                                   headers={"Authorization": f"Bearer {self.EXECUTIVE_PRODUCER}"})
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
