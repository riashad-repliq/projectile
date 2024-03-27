from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.rest.views.user import *

urlpatterns = [
    path('user/all/', ListUserView.as_view(), name='user-list'),
    path('create/', CreateUserView.as_view(), name='create-user'),
    path('details/<uuid:uuid>/', RetrieveUserView.as_view(), name='user-details'),
    path('details/update/<uuid:uuid>/', UpdateUserView.as_view(), name='update-user'),
    path('delete/<uuid:uuid>/', DestroyUserView.as_view(), name='delete-user'),


    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]