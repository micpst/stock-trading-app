from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("register", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/verify", TokenVerifyView.as_view(), name='token_verify'),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
