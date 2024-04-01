from django.urls import path, include

urlpatterns = [
    path('', include('order.rest.urls.order')),


]

