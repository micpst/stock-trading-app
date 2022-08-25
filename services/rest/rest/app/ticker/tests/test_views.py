from django.urls import reverse
from django.utils.http import urlencode
from parameterized import parameterized
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase

from rest.app.user.models import User


class PriceTickersListViewTests(APITestCase):
    fixtures = ["test_users", "test_stocks", "test_price_tickers"]

    def test_read_stock_ticker_prices_without_query_params(self):
        user = User.objects.get(id=1)
        url = reverse("price_tickers_list")

        self.client.force_authenticate(user=user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    @parameterized.expand([
        (1, 3),
        (2, 1),
        (3, 0),
        (4, 0),
    ])
    def test_read_stock_ticker_prices_with_stock_query_param(
        self, stock_id, expected_data_length
    ):
        user = User.objects.get(id=1)
        query_kwargs = {"stock": stock_id}
        url = f"{reverse('price_tickers_list')}?{urlencode(query_kwargs)}"

        self.client.force_authenticate(user=user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), expected_data_length)

    @parameterized.expand([
        ("25-08-2022T00:00:00Z", "26-08-2022T00:00:00Z", 2, HTTP_200_OK),
        ("21-08-2022T00:00:00Z", "", 1, HTTP_400_BAD_REQUEST),
        ("", "21-08-2022T00:00:00Z", 1, HTTP_400_BAD_REQUEST),
    ])
    def test_read_stock_ticker_prices_with_date_range_query_params(
        self, from_date, to_date, expected_data_length, expected_status_code
    ):
        user = User.objects.get(id=1)
        query_kwargs = {
            "stock": 1,
            "from": from_date,
            "to": to_date,
        }
        url = f"{reverse('price_tickers_list')}?{urlencode(query_kwargs)}"

        self.client.force_authenticate(user=user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(len(response.data), expected_data_length)
