from django.test import TestCase
from parameterized import parameterized

from rest.app.account.models import Account


class AccountModelTest(TestCase):
    fixtures = ["test_users", "test_accounts"]

    @parameterized.expand([
        ("user", "user"),
        ("type", "type"),
        ("status", "status"),
        ("balance", "balance"),
        ("currency", "currency"),
    ])
    def test_field_label(self, field_name, expected_label):
        account = Account.objects.get(id=1)
        field_label = account._meta.get_field(field_name).verbose_name
        self.assertEqual(field_label, expected_label)

    @parameterized.expand([
        ("type", 12),
        ("status", 9),
        ("currency", 3),
    ])
    def test_field_max_length(self, field_name, expected_max_length):
        account = Account.objects.get(id=1)
        max_length = account._meta.get_field(field_name).max_length
        self.assertEqual(max_length, expected_max_length)

    def test_balance_field_precision(self):
        account = Account.objects.get(id=1)
        max_digits = account._meta.get_field("balance").max_digits
        decimal_places = account._meta.get_field("balance").decimal_places
        self.assertEqual(max_digits, 19)
        self.assertEqual(decimal_places, 4)
