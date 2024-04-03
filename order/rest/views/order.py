from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from order.models import Order
from order.rest.serializers.order import OrderSerializer

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]

