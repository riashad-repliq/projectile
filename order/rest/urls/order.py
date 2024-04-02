from django.urls import path
from order.rest.views.order import OrderListAPIView , OrderCreateView
urlpatterns = [
    path('/', OrderListAPIView.as_view(), name='cart-detail'),
    path('/checkout', OrderCreateView.as_view(), name='checkout'),

    # path('/items', CartItemListCreateView.as_view(), name='list-create-cart-items'),
]

