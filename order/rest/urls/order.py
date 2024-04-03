from django.urls import path
from order.rest.views.order import OrderListAPIView
urlpatterns = [
    path('/', OrderListAPIView.as_view(), name='orders'),
]

