from django.urls import reverse
from parameterized import parameterized
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from rest_framework.test import APITestCase

from rest.app.user.models import User
from rest.app.stock.models import Stock


class StockListViewTests(APITestCase):
    fixtures = ["test_users", "test_stocks"]

    @parameterized.expand([
        (1, HTTP_201_CREATED, 4),
        (2, HTTP_403_FORBIDDEN, 3),
    ])
    def test_create_stock_with_valid_data(self, user_id, expected_status_code, expected_stock_count):
        user = User.objects.get(id=user_id)
        url = reverse("stocks_list_create")
        stock_data = {"symbol": "VAL.US", "company_name": "Value Company Inc."}

        self.client.force_authenticate(user=user)
        response = self.client.post(url, stock_data)

        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(Stock.objects.count(), expected_stock_count)

    @parameterized.expand([
        (1, HTTP_200_OK),
        (2, HTTP_200_OK),
        (3, HTTP_200_OK),
        (4, HTTP_404_NOT_FOUND),
    ])
    def test_read_stock_data(self, stock_id, expected_status_code):
        user = User.objects.get(id=2)
        kwargs = {"pk": stock_id}
        url = reverse("stock_retrieve_update_delete", kwargs=kwargs)

        self.client.force_authenticate(user=user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, expected_status_code)
