from rest_framework.serializers import ModelSerializer

from rest.app.account.models import Account


class AccountSerializer(ModelSerializer):
    """
    User trading account model serializer.
    """

    class Meta:
        model = Account
        fields = "__all__"
        extra_kwargs = {
            "user": {"write_only": True},
        }
