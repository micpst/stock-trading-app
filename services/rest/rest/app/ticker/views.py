from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from rest.app.ticker.filters import DateRangeFilter, StockFilter
from rest.app.ticker.models import Ticker
from rest.app.ticker.serializers import TickerSerializer


class TickersListView(ListAPIView):
    """
    Lists price ticker model instances.
    """

    filter_backends = (
        StockFilter,
        DateRangeFilter,
    )
    permission_classes = (IsAuthenticated,)
    serializer_class = TickerSerializer
    queryset = Ticker.objects.all()
