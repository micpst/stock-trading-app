from rest_framework.serializers import ModelSerializer

from rest.app.ticker.models import PriceTicker


class PriceTickerSerializer(ModelSerializer):
    """
    Stock price ticker model serializer.
    """

    class Meta:
        model = PriceTicker
        fields = "__all__"
        extra_kwargs = {
            "stock": {"write_only": True},
        }
