from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from order.models import Order, OrderItem
from order.rest.serializers.order import OrderSerializer, CreateOrderSerializer

class OrderListAPIView(ListAPIView):
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer

class OrderCreateView(CreateAPIView):
    serializer_class = CreateOrderSerializer

    def create(self, request):

        selected_cart_items = request.user.cart.cart_items.filter(selected=True)

        if not selected_cart_items:
            return Response({'message': 'No items selected for ordering.'}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = sum(item.calculate_price() for item in selected_cart_items)

        order = Order.objects.create(
            user=request.user,
            total_amount=total_amount,
            delivery_status='pending'
        )

        for cart_item in selected_cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity
            )
            cart_item.delete()
        order_serializer = CreateOrderSerializer(order)
        return Response({'message': 'Order placed successfully.',
                          'order': order_serializer.data
                         }, status=status.HTTP_201_CREATED)