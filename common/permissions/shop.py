from django.shortcuts import get_object_or_404

from rest_framework import permissions
from shop.models import Shop,Member
# from product.rest.views.product import ManageProductView, ManageProductSerializer

class ShopPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        shop_uuid = view.kwargs.get('shop_uuid')
        shop =get_object_or_404(Shop,uuid=shop_uuid)

        #to check if user is a member in a specific shop and noty just any shop
        member = get_object_or_404(Member,user=request.user, shop=shop)
        if member.member_type == 'owner':
            return True

        elif member.member_type == 'admin':
            if request.method == 'POST' and 'member_type' in request.data:
                return request.data['member_type'] in ['manager', 'staff']
            return request.method in ['GET', 'PUT', 'PATCH', 'POST']


        elif member.member_type == 'manager':
            if request.method == 'POST' and 'member_type' in request.data:
                return request.data['member_type'] in ['staff']
            return request.method in ['GET', 'PUT', 'PATCH', 'POST']


        elif member.member_type == 'staff':
            return request.method == 'GET'



class DefaultShopPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        #to check if user is a member in a specific shop and noty just any shop
        member = get_object_or_404(Member,user=request.user, last_visited=True)
        if member.member_type == 'owner':
            return True

        elif member.member_type in ['admin', 'manager']:
            return request.method != 'DELETE'
        elif member.member_type == 'staff':
            return request.method == 'GET'



class ProductPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        shop_uuid = view.kwargs.get('shop_uuid')
        shop =get_object_or_404(Shop,uuid=shop_uuid)

        #to check if user is a member in a specific shop and noty just any shop
        member = get_object_or_404(Member,user=request.user, shop=shop)
        if member.member_type in ['owner', 'admin', 'manager']:
            return True

        elif member.member_type == 'staff':
            return request.method == 'GET'

