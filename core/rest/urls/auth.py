from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),# this sould be in settings.urls files
    path('/refresh', TokenRefreshView.as_view(), name='token_refresh'),# this sould be in settings.urls files
]