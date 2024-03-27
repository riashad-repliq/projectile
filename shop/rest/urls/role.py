from django.urls import path
from shop.rest.views.role import *
urlpatterns = [
    # path('/roles', RoleListCreateView.as_view(), name='roles'),
    # path('/<uuid:uuid>', ManageRoleView.as_view(), name='manage-role'),

    path('/<uuid:uuid>/role', ShopRoleListCreateView.as_view(), name='list-create-shop-roles'),
    path('/<uuid:uuid>/role<uuid', ManageShopRoleView.as_view(), name='manage-shop-roles'),


]
