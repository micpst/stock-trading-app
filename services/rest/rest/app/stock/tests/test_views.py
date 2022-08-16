from parameterized import parameterized
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from rest_framework.test import APITestCase

from rest.app.user.models import User
from rest.app.stock.models import Stock


class StockListViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser(
            email="admin@email.com",
            first_name="Test",
            last_name="Test",
            password="password",
        )
        User.objects.create_user(
            email="test@email.com",
            first_name="Test",
            last_name="Test",
            password="password",
        )
        Stock.objects.create(
            ticker="TEST.US",
            company_name="Test Company Inc.",
        )

    @parameterized.expand([
        (User.objects.get(id=1), HTTP_201_CREATED, 2),
        (User.objects.get(id=2), HTTP_403_FORBIDDEN, 1),
    ])
    def test_create_stock_with_valid_data(self, user, expected_status_code, expected_stock_count):
        stock_data = {
            "ticker": "VAL.US",
            "company_name": "Value Company Inc.",
        }

        self.client.force_authenticate(user=user)
        response = self.client.post("/rest/stocks", stock_data)

        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(Stock.objects.count(), expected_stock_count)

    @parameterized.expand([
        (User.objects.get(id=1),),
        (User.objects.get(id=2),),
    ])
    def test_read_stock_data(self, user):
        expected_response_data = {
            "id": 1,
            "ticker": "TEST.US",
            "company_name": "Test Company Inc.",
            "market_capitalization": "NA",
            "dividend_yield": "NA",
            "eps": "NA",
            "pe": "NA",
            "pb": "NA",
            "de": "NA",
        }

        self.client.force_authenticate(user=user)
        response = self.client.get("/rest/stocks/1")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_response_data)
