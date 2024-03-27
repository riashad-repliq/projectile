from django.urls import path
from shop.rest.views.shop import *
urlpatterns = [
    path('all/', ShopListView.as_view(), name='shops'),
    path('create/', CreateShopView.as_view(), name='create-shop'),
    path('shop/<uuid:uuid>/', DetailShopView.as_view(), name='update-shop'),
    path('shop/update/<uuid:uuid>/', UpdateShopView.as_view(), name='update-shop'),
    path('shop/delete/<uuid:uuid>/', DeleteShopView.as_view(), name='delete-shop'),
]
