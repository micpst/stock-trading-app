from datetime import datetime

from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rest.app.ticker.models import PriceTicker
from rest.app.ticker.serializers import PriceTickerSerializer


class PriceTickersListView(GenericAPIView):
    """
    Lists price ticker model instances.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = PriceTickerSerializer

    def get_queryset(self) -> QuerySet:
        filter_kwargs = {"stock": self.request.query_params.get("stock")}

        from_date = self.request.query_params.get("from")
        to_date = self.request.query_params.get("to")

        if from_date is not None and to_date is not None:
            try:
                from_date = datetime.strptime(from_date, "%d-%m-%YT%H:%M:%SZ")
                to_date = datetime.strptime(to_date, "%d-%m-%YT%H:%M:%SZ")

            except ValueError as e:
                raise ValidationError({"details": e})

            filter_kwargs["time_epoch__range"] = [from_date, to_date]

        return PriceTicker.objects.filter(**filter_kwargs)

    def get(self, request: Request) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
