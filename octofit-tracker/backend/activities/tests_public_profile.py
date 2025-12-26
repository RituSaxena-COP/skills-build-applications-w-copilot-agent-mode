from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()
LIST_URL = '/api/profiles/'
DETAIL_URL = '/api/profiles/{username}/'

class PublicProfileTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.u1 = User.objects.create_user(username='alice', password='passw0rd')
        self.u2 = User.objects.create_user(username='bob', password='passw0rd')
        # ensure profiles exist
        self.u1.profile.bio = 'Runner'
        self.u1.profile.save()
        self.u2.profile.bio = 'Cyclist'
        self.u2.profile.save()

    def test_list_public_profiles(self):
        res = self.client.get(LIST_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsInstance(res.data, list)
        usernames = {p['username'] for p in res.data}
        self.assertIn('alice', usernames)
        self.assertIn('bob', usernames)

    def test_get_public_profile_detail(self):
        res = self.client.get(DETAIL_URL.format(username='alice'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['username'], 'alice')
        self.assertEqual(res.data['bio'], 'Runner')
