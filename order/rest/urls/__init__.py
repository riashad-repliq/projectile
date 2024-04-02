from django.urls import path, include

urlpatterns = [
    path('/me/order', include('order.rest.urls.order')),


]

