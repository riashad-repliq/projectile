from django.urls import path
from shop.rest.views.shop import *
urlpatterns = [
    path('', ShopListCreateView.as_view(), name='shops'),
    path('/<uuid:uuid>', ManageShopView.as_view(), name='manage-shop'),
]
