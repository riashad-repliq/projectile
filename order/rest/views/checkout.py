# from django.shortcuts import get_object_or_404

# from rest_framework import status
# from rest_framework.generics import CreateAPIView

# from product.models import ShopProduct
# from order.models import Order, OrderItem
# from order.rest.serializers.order import OrderSerializer, DirectOrderSerializer

# class CheckoutView(CreateAPIView):

#     def get_serializer_class(self):
#         if 'cart_items' in request.data

#     def create(self, request):
#         if 'cart_items' in request.data:
#             return self.cart_checkout_order(request)

#         else:
#             return self.direct_order(request)

#     def cart_checkout_order(self, request):
#         serializer = OrderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         order = serializer.save(user= request.user)


#     def direct_order(self, request):
#         serializer = DirectOrderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         shop_product_uuid = serializer.validated_data['shop_product_uuid']
#         shop_product = get_object_or_404(ShopProduct, uuid = shop_product_uuid)
#         quantity = serializer.validated_data['quantity']
#         total_price = shop_product.product.price * quantity
#         order = Order.objects.create(user=request.user, total_amount=total_price, delivery_status='pending')

#         OrderItem.objects.create(order=order, quantity=quantity, price=total_price)
