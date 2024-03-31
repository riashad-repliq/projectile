from django.urls import path
from cart.rest.views.cart_item import *
urlpatterns = [
    path('/me/cart/items', CartItemListCreateView.as_view(), name='list-create-cart-items'),
    path('/me/cart/items/<uuid:cart_item_uuid>', ManageCartItemView.as_view(), name='manage-cart-item'),

]
