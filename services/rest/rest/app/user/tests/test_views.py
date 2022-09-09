from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase

from rest.app.user.models import User


class UserRegisterViewTests(APITestCase):
    fixtures = ["test_users"]

    def test_create_user_with_valid_data(self):
        url = reverse("user_register")
        user_data = {
            "email": "test@email.com",
            "first_name": "Test",
            "last_name": "Test",
            "password": "password",
        }

        response = self.client.post(url, user_data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertIsNotNone(response.data["tokens"]["refresh"])
        self.assertIsNotNone(response.data["tokens"]["access"])
        self.assertEqual(User.objects.count(), 3)

    def test_create_user_with_existing_email(self):
        url = reverse("user_register")
        user_data = {
            "email": "test@test.com",
            "first_name": "Test",
            "last_name": "Test",
            "password": "password",
        }
        expected_response_data = {
            "email": ["user with this email address already exists."]
        }

        response = self.client.post(url, user_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_data)
        self.assertEqual(User.objects.count(), 2)
