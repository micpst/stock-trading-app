from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase

from rest.app.user.models import User


class UserRegisterViewTests(APITestCase):
    def test_create_user_with_valid_data(self):
        user_data = {
            "email": "test@email.com",
            "first_name": "Test",
            "last_name": "Test",
            "password": "password",
        }

        response = self.client.post("/rest/auth/register", user_data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertIsNotNone(response.data["tokens"]["refresh"])
        self.assertIsNotNone(response.data["tokens"]["access"])
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_with_existing_data(self):
        user_data = {
            "email": "test@email.com",
            "first_name": "Test",
            "last_name": "Test",
            "password": "password",
        }
        expected_response_data = {
            "email": ["user with this email address already exists."]
        }
        User.objects.create_user(**user_data)

        response = self.client.post("/rest/auth/register", user_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_data)
        self.assertEqual(User.objects.count(), 1)
