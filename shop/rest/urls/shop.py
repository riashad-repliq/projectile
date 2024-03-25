from django.urls import path
from shop.rest.views.shop import *
urlpatterns = [
    path('all/', ShopListView.as_view(), name='shops'),
    path('shop/<str:pk>', ManageShopView.as_view(), name='update-shop'),
    path('shop/delete/<str:pk>', DeleteShopView.as_view(), name='delete-shop'),
]
