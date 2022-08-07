from typing import Dict

from rest_framework.serializers import SerializerMethodField, ModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from rest.app.user.models import User


class UserRegisterSerializer(ModelSerializer):
    """
    Custom User model serializer.
    """

    tokens = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
            "tokens",
        )
        extra_kwargs = {
            "email": {"write_only": True},
            "first_name": {"write_only": True},
            "last_name": {"write_only": True},
            "password": {"write_only": True},
        }

    def get_tokens(self, obj: User) -> Dict[str, str]:
        refresh = RefreshToken.for_user(obj)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
