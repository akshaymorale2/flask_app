import sys
sys.path.append(r"/home/circleci/project/social_app/tests/")
import json
from .. import db
from ..social import create_app
from unittest import TestCase


class TestView(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        db.create_all(app=self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app)

    def test_signup_user(self):
        payload_register = json.dumps({
            'contactNumber': "9822902121",
            'dateOfBirth': "2008-07-05T18:30:00.000Z",
            'email': "ironman@gmail.com",
            'first_name': "Robert",
            'gender': "Male",
            'is_verified': True,
            'last_name': "Downey",
            'password': "12345",
            'username': "ironman"
        })
        response = self.client.post('/user/register', headers={"Content-Type": "application/json"}, data=payload_register)
        # success
        assert response.status_code == 200

    def test_social_login_user(self):
        payload = json.dumps({
            'contactNumber': "9022902121",
            'dateOfBirth': "1992-07-05T18:30:00.000Z",
            'email': "minato@gmail.com",
            'first_name': "Minato",
            'gender': "Male",
            'is_verified': True,
            'last_name': "Uzumaki",
            'password': "12345",
            'username': "minato"
        })

        payload_login = json.dumps({
            'username': 'minato',
            'password': "12345"
        })
        self.client.post('/user/register', headers={"Content-Type": "application/json"}, data=payload)
        response_login = self.client.post('/user/login', headers={"Content-Type": "application/json"}, data=payload_login)

        # success
        assert response_login.status_code == 200

