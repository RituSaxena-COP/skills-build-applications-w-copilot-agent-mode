from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Activity
from django.utils import timezone
from rest_framework import status

User = get_user_model()

API_ACTIVITIES = '/api/activities/'

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')

    def test_create_activity(self):
        now = timezone.now()
        Activity.objects.create(user=self.user, activity_type='run', duration_minutes=30, distance_km=5.0, timestamp=now)
        self.assertEqual(Activity.objects.count(), 1)
        a = Activity.objects.first()
        self.assertEqual(a.user, self.user)
        self.assertEqual(a.activity_type, 'run')

class ActivityAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiuser', password='pass')
        self.client = APIClient()

    def test_list_requires_auth(self):
        res = self.client.get(API_ACTIVITIES)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_and_list_activity(self):
        self.client.force_authenticate(user=self.user)
        now = timezone.now().isoformat()
        payload = {
            'activity_type': 'walk',
            'duration_minutes': 20,
            'distance_km': 1.2,
            'notes': 'Nice walk',
            'timestamp': now,
        }
        res = self.client.post(API_ACTIVITIES, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # user should only see their own activities
        res = self.client.get(API_ACTIVITIES)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
