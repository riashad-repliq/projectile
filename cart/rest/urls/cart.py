from django.urls import path
from cart.rest.views.cart import *
urlpatterns = [
    path('/me/cart', CartDetailView.as_view(), name='cart-detail'),

]

