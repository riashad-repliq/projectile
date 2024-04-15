from django.urls import path
from order.rest.views.order import OrderListAPIView, OrderItemListAPIView, OrderItemManageView
urlpatterns = [
    path('', OrderListAPIView.as_view(), name='orders'),
    path('/items', OrderItemListAPIView.as_view(), name='order-items'),
    path('/items/<uuid:order_item_uuid>', OrderItemManageView.as_view(), name='order-items-detail'),
]

