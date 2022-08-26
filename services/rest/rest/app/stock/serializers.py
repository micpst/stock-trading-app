from collections import OrderedDict

from rest_framework.serializers import ModelSerializer

from rest.app.stock.models import Stock


class StockSerializer(ModelSerializer):
    """
    Stock company information model serializer.
    """

    class Meta:
        model = Stock
        fields = "__all__"

    def to_representation(self, instance: Stock) -> OrderedDict:
        result = super().to_representation(instance)
        return OrderedDict(
            [(key, result[key] or "NA") for key in result]
        )
