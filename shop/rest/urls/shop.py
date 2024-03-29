from django.urls import path
from shop.rest.views.shop import *
urlpatterns = [
    path('/we/shops/<uuid:uuid>', ManageShopView.as_view(), name='manage-shop'),





    path('/me/shops', ShopListCreateView.as_view(), name='shops'),
    path('/me/shops/<uuid:uuid>', RetrieveShopView.as_view(), name='retrieve-shop'),

]
