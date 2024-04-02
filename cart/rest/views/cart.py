from django.shortcuts import get_object_or_404

from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from cart.models import Cart, CartItem

from cart.rest.serializers.cart import CartSerializer
from cart.rest.serializers.cart import ManageCartItemSerializer, ListCreateCartItemSerializer

class CartDetailView(RetrieveAPIView):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.cart



class CartItemListCreateView(ListCreateAPIView):
    serializer_class = ListCreateCartItemSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        cart_items = CartItem.objects.filter(cart__user=self.request.user)
        return cart_items


class ManageCartItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = ManageCartItemSerializer
    permission_classes = [IsAuthenticated]
    queryset= CartItem.objects.filter()

    def get_object(self):
        cart_item_uuid = self.kwargs.get('cart_item_uuid')
        cart_item = get_object_or_404 (CartItem, uuid = cart_item_uuid)
        return cart_item
