from django.urls import path
from product.rest.views.shop_product import *
urlpatterns = [
    #Private URLs
    path('/we/shops/<uuid:shop_uuid>/new_product', CreateNewProduct.as_view() ,name='new-products'),

    path('/we/shops/<uuid:shop_uuid>/shop_products', ShopProductListCreateView.as_view(), name='list-create-shop-products'),
    path('/we/shops/<uuid:shop_uuid>/shop_products/<uuid:shop_product_uuid>', ManageShopProductView.as_view(), name='manage-shop-products'),




    #Public URLs
    path('/me/shops/<slug:shop_slug>/shop_products', ListShopProductView.as_view(), name='list-shop-products'),
    path('/me/shops/<slug:shop_slug>/shop_products/<slug:shop_product_slug>', RetrieveShopProductView.as_view(), name='list-create-shop-products')

]

