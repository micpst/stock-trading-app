from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAdminUserOrReadOnly(IsAdminUser):
    """
    The request is authenticated as an admin user, or is a read-only request.
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin
