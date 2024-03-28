from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.rest.views.user import *

urlpatterns = [
    path('', ListCreateUserView.as_view(), name='user-list'),
    path('<uuid:uuid>', ManageUserView.as_view(), name='user-details'),



    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]