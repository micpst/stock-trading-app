from itertools import groupby
from typing import Any, Dict, List

from django.db.models import QuerySet
from rest_framework.serializers import ListSerializer, ModelSerializer

from rest.app.ticker.models import Ticker


class TickerListSerializer(ListSerializer):
    """
    Stock price ticker list serializer.
    """

    def to_representation(self, data: QuerySet) -> List[Dict[str, Any]]:
        return [
            {
                "stock": key,
                "tickers": super(TickerListSerializer, self).to_representation(group),
            }
            for key, group in groupby(data, lambda x: x.stock.id)
        ]


class TickerSerializer(ModelSerializer):
    """
    Stock price ticker model serializer.
    """

    class Meta:
        model = Ticker
        fields = "__all__"
        extra_kwargs = {
            "stock": {"write_only": True},
        }
        list_serializer_class = TickerListSerializer
