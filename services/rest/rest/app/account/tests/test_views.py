from django.urls import reverse
from parameterized import parameterized
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from rest_framework.test import APITestCase

from rest.app.user.models import User


class AccountSelectViewTests(APITestCase):
    fixtures = ["test_users", "test_accounts"]

    @parameterized.expand([
        (2, 1, HTTP_200_OK),
        (2, 3, HTTP_404_NOT_FOUND),
        (1, 1, HTTP_403_FORBIDDEN),
    ])
    def test_select_account(self, user_id, account_id, expected_status_code):
        user = User.objects.get(id=user_id)
        kwargs = {"pk": account_id}
        url = reverse("account_select", kwargs=kwargs)

        self.client.force_authenticate(user=user)
        response = self.client.post(url)

        self.assertEqual(response.status_code, expected_status_code)
