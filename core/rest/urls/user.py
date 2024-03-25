from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.rest.views.user import *

urlpatterns = [

    path('create/', CreateUserView.as_view(), name='create-user'),
    path('details/<int:pk>', ManageUserView.as_view(), name='user-details'),
    path('delete/<int:pk>', DestroyUserView.as_view(), name='delete-user'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]