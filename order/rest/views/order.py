
from rest_framework.generics import ListAPIView
from order.models import Order, OrderItem
from order.rest.serializers.order import OrderSerializer

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

# class OrderDetailAPIView(RetrieveAPIView):
#     queryset = Order.objects.filter()
#     serializer_class = OrderSerializer

