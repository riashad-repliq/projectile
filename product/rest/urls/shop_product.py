from django.urls import path
from product.rest.views.shop_product import *
urlpatterns = [
    #Private URLs
    path('/we/shops/<uuid:shop_uuid>/shop_products', ShopProductListCreateView.as_view(), name='list-create-shop-products'),
    path('/we/shops/<uuid:shop_uuid>/shop_products/<uuid:shop_product_uuid>', ManageShopProductView.as_view(), name='manage-shop-products'),

    path('/we/shops/<uuid:shop_uuid>/new_product', CreateNewProduct.as_view() ,name='new-products')
    #Public URLs


]

