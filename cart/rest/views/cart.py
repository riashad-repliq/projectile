from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from cart.rest.serializers.cart import CartSerializer

class CartDetailView(RetrieveAPIView):
    queryset = Cart.objects.filter()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.cart