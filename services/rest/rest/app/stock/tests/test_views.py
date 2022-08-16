from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase

from rest.app.stock.models import Stock


class StockListViewTests(APITestCase):
    def test_create_stock_with_valid_data(self):
        stock_data = {
            "ticker": "TEST.US",
            "company_name": "Test Company Inc.",
        }

        response = self.client.post("/rest/stocks", stock_data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Stock.objects.count(), 1)

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
        reverse()
        response = self.client.post("/rest/auth/register", user_data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response_data)
        self.assertEqual(User.objects.count(), 1)
