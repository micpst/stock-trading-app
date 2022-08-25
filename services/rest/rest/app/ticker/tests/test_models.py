from datetime import datetime

from django.test import TestCase
from parameterized import parameterized

from rest.app.stock.models import Stock
from rest.app.ticker.models import PriceTicker


class PriceTickerModelTest(TestCase):
    fixtures = ["test_stocks", "test_price_tickers"]

    @parameterized.expand([
        ("stock", "stock"),
        ("price", "price"),
        ("time_epoch", "time epoch"),
    ])
    def test_field_label(self, field_name, expected_label):
        price_ticker = PriceTicker.objects.get(id=1)
        field_label = price_ticker._meta.get_field(field_name).verbose_name
        self.assertEqual(field_label, expected_label)

    def test_price_precision(self):
        price_ticker = PriceTicker.objects.get(id=1)
        max_digits = price_ticker._meta.get_field("price").max_digits
        decimal_places = price_ticker._meta.get_field("price").decimal_places
        self.assertEqual(max_digits, 19)
        self.assertEqual(decimal_places, 4)
