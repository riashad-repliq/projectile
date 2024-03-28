from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django.shortcuts import render
from shop.models import Shop, Member
from shop.rest.serializers.member import MemberSerializer
from rest_framework.exceptions import NotFound

"""will add permissions classes for all views at the end"""

class ShopMemberListCreateView(ListCreateAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        shop_uuid = self.kwargs.get('shop_uuid')

        try:
            shop = Shop.objects.get(uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")

        # Getting member
        members = Member.objects.filter(shop=shop)
        if not members:
            raise NotFound(detail="This shop does not have any members")

        return members

class ManageShopMemberView(RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.filter()

    def get_object(self):
        shop_uuid = self.kwargs.get('shop_uuid')

        try:
            shop = Shop.objects.get(uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")

        #  Getting member uuid
        member_uuid = self.kwargs.get('member_uuid', None)

        try:
            member = Member.objects.get(uuid=member_uuid)
        except Member.DoesNotExist:
            raise NotFound(detail="Member does not exist")


        return member

