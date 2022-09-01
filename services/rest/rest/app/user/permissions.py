from typing import Type

from django.db.models import Model
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAdminUserOrReadOnly(IsAdminUser):
    """
    The request is authenticated as an admin user, or is a read-only request.
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        is_admin = super().has_permission(request, view)
        return bool(request.method in SAFE_METHODS or is_admin)


class IsOwner(BasePermission):
    """
    Allows only user who own the object to access it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request: Request, view: APIView, obj: Type[Model]) -> bool:
        return bool(
            request.user
            and obj.user
            and obj.user == request.user
        )


class IsCreatedByAccount(BasePermission):
    """
    Allows only user with selected account that created the object to access it.
    Assumes the model instance has an `account` attribute.
    """

    def has_object_permission(self, request: Request, view: APIView, obj: Type[Model]) -> bool:
        return bool(
            request.user
            and request.user.account
            and obj.account
            and obj.account == request.user.account
        )
