from rest_framework.serializers import ModelSerializer

from rest.app.order.models import Order


class OrderSerializer(ModelSerializer):
    """
    Order model serializer.
    """

    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {
            "account": {"write_only": True},
        }
