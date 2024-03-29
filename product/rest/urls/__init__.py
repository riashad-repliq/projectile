from django.urls import path, include

urlpatterns = [
    path('', include('product.rest.urls.shop_product')),
    # path('', include('product.rest.urls.member')),

]

