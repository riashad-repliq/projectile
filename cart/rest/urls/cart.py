from django.urls import path
from cart.rest.views.cart import *
from cart.rest.views.cart import *
urlpatterns = [
    path('/me/cart/', CartDetailView.as_view(), name='cart-detail'),

    path('/me/cart/items', CartItemListCreateView.as_view(), name='list-create-cart-items'),
    path('/me/cart/items/<uuid:cart_item_uuid>', ManageCartItemView.as_view(), name='manage-cart-item'),

]




