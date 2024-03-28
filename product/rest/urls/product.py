from django.urls import path
from product.rest.views.product import *
urlpatterns = [
    path('', ProductListCreateView.as_view(), name='products'),
    path('<uuid:uuid>', ManageProductView.as_view(), name='manage-product'),

]
