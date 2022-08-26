from typing import Any

from django.db.models import QuerySet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from rest.app.order.models import Order
from rest.app.stock.serializers import StockSerializer


class OrdersListView(GenericAPIView):
    """
    Creates and lists Order model instances.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = StockSerializer

    def get_queryset(self) -> QuerySet:
        pass

    def get(self, request: Request) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class OrderDetailsView(GenericAPIView):
    """
    Updates and deletes Order model instance.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = StockSerializer

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
