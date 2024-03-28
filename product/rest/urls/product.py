from django.urls import path
from product.rest.views.shop_product import *
urlpatterns = [
    path('shops/<uuid:shop_uuid>/products', ShopProductListCreateView.as_view(), name='list-create-shop-members'),
    path('shops/<uuid:shop_uuid>/products/<uuid:product_uuid>', ManageShopProductView.as_view(), name='manage-shop-members'),

]

