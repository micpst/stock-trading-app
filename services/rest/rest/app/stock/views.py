from typing import Any

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from rest.app.stock.models import Stock
from rest.app.stock.serializers import StockSerializer
from rest.app.user.permissions import IsAdminUserOrReadOnly


class StocksListView(GenericAPIView):
    """
    Creates and lists Stock model instances.
    """

    permission_classes = (
        IsAdminUserOrReadOnly,
        IsAuthenticated,
    )
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    def get(self, request: Request) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class StockDetailsView(GenericAPIView):
    """
    Retrieves, updates and deletes Stock model instance.
    """

    permission_classes = (
        IsAdminUserOrReadOnly,
        IsAuthenticated,
    )
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)

    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
