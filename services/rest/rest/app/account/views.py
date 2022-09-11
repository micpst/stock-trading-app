from typing import Any

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rest.app.account.models import Account
from rest.app.account.serializers import AccountSerializer
from rest.app.user.filters import OwnerFilter
from rest.app.user.permissions import IsOwner


class AccountsListView(ListCreateAPIView):
    """
    Creates and lists Account model instances.
    """

    filter_backends = (OwnerFilter,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountDetailsView(RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates and deletes Account model instance.
    """

    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountSelectView(GenericAPIView):
    """
    Selects Account model instance for authenticated user.
    """

    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
    queryset = Account.objects.all()

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        request.user.update(account=instance)
        return Response(status=HTTP_200_OK)
