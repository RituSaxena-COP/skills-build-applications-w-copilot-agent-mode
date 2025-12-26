from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

REG_URL = '/api/auth/registration/'
LOGIN_URL = '/api/auth/login/'

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'newuser'
        self.password = 'strong-pass-123'

    def test_registration_creates_user(self):
        payload = {
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
        }
        res = self.client.post(REG_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # Avoid DB queries that can trigger djongo SQL parsing edge-cases in tests;
        # verify registration by attempting to login with the new credentials.
        login_res = self.client.post(LOGIN_URL, {'username': self.username, 'password': self.password})
        self.assertEqual(login_res.status_code, status.HTTP_200_OK)
        self.assertIn('key', login_res.data)

    def test_login_returns_token(self):
        User.objects.create_user(username=self.username, password=self.password)
        payload = {
            'username': self.username,
            'password': self.password,
        }
        res = self.client.post(LOGIN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # dj-rest-auth with TokenAuthentication returns 'key'
        self.assertIn('key', res.data)
