from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from cart.models import  CartItem
from cart.rest.serializers.cart_item import ManageCartItemSerializer, ListCreateCartItemSerializer

class CartItemListCreateView(ListCreateAPIView):
    serializer_class = ListCreateCartItemSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        cart_items = CartItem.objects.filter(cart__user=self.request.user)
        return cart_items


class ManageCartItemView(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.filter()
    serializer_class = ManageCartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart_item_uuid = self.kwargs.get('cart_item_uuid')
        cart_item = get_object_or_404 (CartItem, uuid = cart_item_uuid)
        return cart_item