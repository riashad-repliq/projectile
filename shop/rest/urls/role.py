from django.urls import path
from shop.rest.views.role import *
urlpatterns = [
    path('roles/all', RoleListView.as_view(), name='roles'),
    path('role/create', CreateRoleView.as_view(), name='create-role'),
    path('role/<uuid:uuid>', DetailRoleView.as_view(), name='update-role'),
    path('role/update/<uuid:uuid>', UpdateRoleView.as_view(), name='delete-role'),
    path('role/delete/<uuid:uuid>', DeleteRoleView.as_view(), name='delete-role'),
]
