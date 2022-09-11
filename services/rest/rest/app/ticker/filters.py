from datetime import datetime

from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request
from rest_framework.views import APIView


class StockFilter(BaseFilterBackend):
    """
    Filters queryset based on specified stock ids.
    Query params:
    * stocks - Retrieve data rows related to specified stocks.
    """

    def filter_queryset(self, request: Request, queryset: QuerySet, view: APIView) -> QuerySet:
        stocks = request.query_params.get("stocks")
        filter_kwargs = {}

        if stocks is not None:
            try:
                filter_kwargs["stock__in"] = [int(stock) for stock in stocks.split(",")]
            except ValueError as e:
                raise ValidationError({"details": e})

        return queryset.filter(**filter_kwargs)


class DateRangeFilter(BaseFilterBackend):
    """
    Filters queryset based on specified date range.
    Query params:
    * from_date - Retrieve data rows on and after the specified start date.
    * to_date - Retrieve data rows up to and including the specified end date.
    """

    def filter_queryset(self, request: Request, queryset: QuerySet, view: APIView) -> QuerySet:
        from_date = request.query_params.get("from_date")
        to_date = request.query_params.get("to_date")
        date_format = "%d-%m-%YT%H:%M:%SZ"
        filter_kwargs = {}

        try:
            if from_date is not None:
                filter_kwargs["time_epoch__gte"] = datetime.strptime(from_date, date_format)
            if to_date is not None:
                filter_kwargs["time_epoch__lte"] = datetime.strptime(to_date, date_format)
        except ValueError as e:
            raise ValidationError({"details": e})

        return queryset.filter(**filter_kwargs)
