from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied


from rest_framework import permissions
from rest_framework.exceptions import NotFound
from shop.models import Shop,Member


class CustomGetObjectOr404:
    @classmethod
    def get_object_or_404(cls, klass, *args, **kwargs):
        manager = klass._default_manager if hasattr(klass, '_default_manager') else klass.objects
        queryset = manager.get_queryset()
        try:
            return queryset.get(*args, **kwargs)
        except queryset.model.DoesNotExist:
            raise PermissionDenied("Permission Denied")


class ShopPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        shop_uuid = view.kwargs.get('shop_uuid')
        shop =get_object_or_404(Shop,uuid=shop_uuid)

        member = CustomGetObjectOr404.get_object_or_404(Member,user=request.user, shop=shop)
        # try:
        #     member =Member.objects.get(shop=shop, user=request.user)
        # except:
        #     return False

        if member.member_type == 'owner':
            return True

        elif member.member_type == 'admin':
            if request.method in ['POST', 'PATCH'] and 'member_type' in request.data:
                return request.data['member_type'] in ['manager', 'staff']


        elif member.member_type == 'manager':
            if request.method in ['POST', 'PATCH'] and 'member_type' in request.data:
                return request.data['member_type'] in ['staff']
            # return request.method in ['GET', 'PUT', 'PATCH', 'POST']


        elif member.member_type == 'staff':
            return request.method == 'GET'

        return request.method in ['GET', 'PUT', 'PATCH', 'POST']



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

