from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()
PROFILE_URL = '/api/profile/'
REG_URL = '/api/auth/registration/'

class ProfileTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'profileuser'
        self.password = 'pw123456'

    def test_profile_auto_created_on_registration(self):
        payload = {'username': self.username, 'password1': self.password, 'password2': self.password}
        res = self.client.post(REG_URL, payload)
        if res.status_code != status.HTTP_201_CREATED:
            self.fail(f"Registration failed: {res.status_code} {res.data}")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # login and GET profile
        login_res = self.client.post('/api/auth/login/', {'username': self.username, 'password': self.password})
        self.assertEqual(login_res.status_code, status.HTTP_200_OK)
        token = login_res.data.get('key')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        res = self.client.get(PROFILE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['user'], self.username)

    def test_update_profile(self):
        user = User.objects.create_user(username=self.username, password=self.password)
        # manual profile should already exist due to signals, but ensure
        # create if missing
        if not hasattr(user, 'profile'):
            from activities.models import Profile
            Profile.objects.create(user=user)
        login_res = self.client.post('/api/auth/login/', {'username': self.username, 'password': self.password})
        token = login_res.data.get('key')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        patch_res = self.client.patch(PROFILE_URL, {'bio': 'Hello profile'}, format='json')
        self.assertEqual(patch_res.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_res.data['bio'], 'Hello profile')
