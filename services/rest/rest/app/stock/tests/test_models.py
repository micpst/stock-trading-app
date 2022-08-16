from django.test import TestCase
from parameterized import parameterized

from rest.app.stock.models import Stock


class StockModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Stock.objects.create(
            ticker="TEST.US",
            company_name="Test Company Inc.",
            market_capitalization=1_000_000_000_000.00,
            dividend_yield=0.00,
            eps=12.45,
            pe=32.00,
            pb=4.00,
            de=1.20,
        )

    @parameterized.expand([
        ("ticker", "ticker"),
        ("company_name", "company name"),
        ("market_capitalization", "market capitalization"),
        ("dividend_yield", "dividend yield"),
        ("eps", "eps"),
        ("pe", "pe"),
        ("pb", "pb"),
        ("de", "de"),
    ])
    def test_field_label(self, field_name, expected_label):
        stock = Stock.objects.get(id=1)
        field_label = stock._meta.get_field(field_name).verbose_name
        self.assertEqual(field_label, expected_label)

    @parameterized.expand([
        ("ticker", 10),
        ("company_name", 255),
    ])
    def test_field_max_length(self, field_name, expected_max_length):
        stock = Stock.objects.get(id=1)
        max_length = stock._meta.get_field(field_name).max_length
        self.assertEqual(max_length, expected_max_length)

    @parameterized.expand([
        ("market_capitalization", 19, 2),
        ("dividend_yield", 19, 2),
        ("eps", 19, 2),
        ("pe", 19, 2),
        ("pb", 19, 2),
        ("de", 19, 2),
    ])
    def test_field_precision(self, field_name, expected_max_digits, expected_decimal_places):
        stock = Stock.objects.get(id=1)
        max_digits = stock._meta.get_field(field_name).max_digits
        decimal_places = stock._meta.get_field(field_name).decimal_places
        self.assertEqual(max_digits, expected_max_digits)
        self.assertEqual(decimal_places, expected_decimal_places)

    def test_object_name_is_ticker(self):
        stock = Stock.objects.get(id=1)
        self.assertEqual(str(stock), stock.ticker)
