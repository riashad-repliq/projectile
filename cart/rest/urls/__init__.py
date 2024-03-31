from django.urls import path, include

urlpatterns = [
    path('', include('cart.rest.urls.cart')),
    path('', include('cart.rest.urls.cart_item')),

]

