from typing import Any

from django.db.models import QuerySet
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rest.app.order.models import Order, OrderStatus
from rest.app.order.serializers import OrderSerializer
from rest.app.user.permissions import IsCreatedByAccount


class OrdersListView(ListAPIView):
    """
    Lists Order model instances.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Order.objects.filter(account=user.account)


class OrderPlaceView(CreateAPIView):
    """
    Places new Order model instance in the orderbook.
    """

    permission_classes = (
        IsAuthenticated,
        IsCreatedByAccount,
    )
    serializer_class = OrderSerializer


class OrderCancelView(GenericAPIView):
    """
    Cancels Order model instance.
    """

    permission_classes = (
        IsAuthenticated,
        IsCreatedByAccount,
    )
    queryset = Order.objects.all()

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        instance.update(status=OrderStatus.CANCELLED)
        return Response(status=HTTP_200_OK)
