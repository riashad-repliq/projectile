from django.urls import path, include

urlpatterns = [
    path('', include('cart.rest.urls.cart')),


]

