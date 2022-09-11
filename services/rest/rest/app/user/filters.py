from django.db.models import QuerySet
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request
from rest_framework.views import APIView


class OwnerFilter(BaseFilterBackend):
    """
    Filters queryset based on ownership of the authenticated user.
    """

    def filter_queryset(self, request: Request, queryset: QuerySet, view: APIView) -> QuerySet:
        return queryset.filter(user=request.user)
