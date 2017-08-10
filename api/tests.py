from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class TaskTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create_superuser(
            username="TestName",
            email='a@test.com',
            password="test123",
        )
        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()

    def test_api_create_task(self):
        """Test the api has task creation capability."""
        self.client.force_login(user=self.user)
        response = self.client.post(
            '/tasks/',
            data={'name': "Test task"},
            format='json',
            HTTP_AUTHORIZATION=self.token,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get(
            '/tasks/',
            kwargs={'pk': 1},
            format="json",
        )

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_get_task(self):
        """Test that the api can get one task."""
        self.client.force_login(user=self.user)
        response = self.client.get(
            '/tasks/',
            kwargs={'pk': "1"},
            format="json",
            HTTP_AUTHORIZATION=self.token,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_get_all_task(self):
        """Test that the api can get all task."""
        self.client.force_login(user=self.user)
        response = self.client.get(
            '/tasks/',
            format='json',
            HTTP_AUTHORIZATION=self.token,
        )

        self.assertEqual(response.status_code, 200)
