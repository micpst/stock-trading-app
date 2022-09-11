from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from rest.app.user.serializers import UserRegisterSerializer


class UserRegisterView(CreateAPIView):
    """
    Creates User model instance and returns an access and refresh JSON web token pair.
    """

    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer
