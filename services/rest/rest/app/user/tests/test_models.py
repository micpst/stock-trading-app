from django.test import TestCase
from parameterized import parameterized

from rest.app.user.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email="test@email.com",
            first_name="Test",
            last_name="Test",
            password="password",
        )

    @parameterized.expand(
        [
            ("email", "email address"),
            ("first_name", "first name"),
            ("last_name", "last name"),
            ("password", "password"),
        ]
    )
    def test_field_label(self, field_name, expected_label):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field(field_name).verbose_name
        self.assertEqual(field_label, expected_label)

    @parameterized.expand(
        [
            ("email", 254),
            ("first_name", 150),
            ("last_name", 150),
            ("password", 128),
        ]
    )
    def test_field_max_length(self, field_name, expected_max_length):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field(field_name).max_length
        self.assertEqual(max_length, expected_max_length)

    def test_object_name_is_email(self):
        user = User.objects.get(id=1)
        self.assertEqual(str(user), user.email)
