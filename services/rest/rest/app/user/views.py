from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from rest.app.user.serializers import UserRegisterSerializer


class UserRegisterView(GenericAPIView):
    """
    Takes a set of user data, saves new user in the database
    and returns an access and refresh JSON web token pair.
    """

    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
