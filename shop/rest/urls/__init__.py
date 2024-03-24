from django.urls import path, include

urlpatterns = [
    path('', include('shop.rest.urls.shop')),
]

