from django.urls import path
from shop.rest.views.member import *
urlpatterns = [
    path('<uuid:shop_uuid>/members', ShopMemberListCreateView.as_view(), name='list-create-shop-members'),
    path('<uuid:shop_uuid>/members/<uuid:member_uuid>', ManageShopMemberView.as_view(), name='manage-shop-members'),


]
