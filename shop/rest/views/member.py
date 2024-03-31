from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django.shortcuts import render, get_object_or_404
from common.permissions.shop import *
from shop.models import Shop, Member
from shop.rest.serializers.member import ListCreateMemberSerializer, ManageMemberSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated


class ShopMemberListCreateView(ListCreateAPIView):
    serializer_class = ListCreateMemberSerializer
    permission_classes = [ShopPermission]


    def get_queryset(self):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)

        # Getting member
        members = Member.objects.filter(shop=shop)
        if not members:
            raise NotFound(detail="This shop does not have any members")

        return members
    def perform_create(self, serializer):
        shop_uuid = self.kwargs.get('shop_uuid')
        shop = get_object_or_404(Shop, uuid=shop_uuid)
        serializer.save(shop=shop)


class ManageShopMemberView(RetrieveUpdateDestroyAPIView):
    serializer_class = ManageMemberSerializer
    queryset = Member.objects.filter()

    permission_classes = [ShopPermission]

    def get_object(self):
        shop_uuid = self.kwargs.get('shop_uuid')

        try:
            shop = get_object_or_404(Shop, uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")

        #  Getting member uuid
        member_uuid = self.kwargs.get('member_uuid', None)

        try:
            member = get_object_or_404(Member,uuid=member_uuid)
        except Member.DoesNotExist:
            raise NotFound(detail="Member does not exist")


        return member