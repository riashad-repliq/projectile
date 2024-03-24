from django.urls import path
from shop.rest.views.role import *
urlpatterns = [
    path('roles/', RoleListView.as_view(), name='roles'),
]
