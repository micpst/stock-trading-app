from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest.app.stock.models import Stock
from rest.app.stock.serializers import StockSerializer
from rest.app.user.permissions import IsAdminUserOrReadOnly


class StocksListView(ListCreateAPIView):
    """
    Creates and lists Stock model instances.
    """

    permission_classes = (
        IsAdminUserOrReadOnly,
        IsAuthenticated,
    )
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


class StockDetailsView(RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates and deletes Stock model instance.
    """

    permission_classes = (
        IsAdminUserOrReadOnly,
        IsAuthenticated,
    )
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
