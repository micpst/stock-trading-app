from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest.app.user.views import UserRegisterView

urlpatterns = [
    path("register", UserRegisterView.as_view(), name="user_register"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/verify", TokenVerifyView.as_view(), name='token_verify'),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
