from rest_framework import routers
from .views.views_auth import UserViewSet, RegisterView, EmailVerifyView, RequestPasswordResetView, PasswordResetView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', EmailVerifyView.as_view(), name='user_verify'),
    path('password-reset-request/', RequestPasswordResetView.as_view(), name='request_password_reset'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]

router = routers.SimpleRouter()

router.register(r'user', UserViewSet)

urlpatterns += router.urls
