from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import NotFound

from shop.models import Shop,Member

class ShopPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        shop_uuid = view.kwargs.get('shop_uuid')
        try:
            shop =get_object_or_404(Shop,uuid=shop_uuid)
        except :
            raise NotFound(detail="Shop does not exist")

        try:
            #to check if user is a member in a specific shop and noty just any shop
            member = get_object_or_404(Member,user=request.user, shop=shop)
            if member.member_type == 'owner':
                return True

            elif member.member_type in ['admin', 'manager']:
                return request.method != 'DELETE'
            elif member.member_type == 'staff':
                return request.method == 'GET'

        except :
            raise NotFound(detail="You do not have the permission to access this page")



class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            shop_uuid = view.kwargs.get('uuid')
            try:
                shop = get_object_or_404(Shop, uuid=shop_uuid)
            except Shop.DoesNotExist:
                raise NotFound(detail="Shop does not exist")
            try:
                #to check if user is a member in a specific shop and not just any shop
                member = get_object_or_404(Member,user=request.user, shop=shop)
                if member.member_type == 'owner':
                    return True

            except Member.DoesNotExist:
                    raise NotFound(detail="request.user is not a member of this shop")

        return False



class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        shop_uuid = view.kwargs.get('uuid')
        try:
            shop = get_object_or_404(Shop, uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")
        try:
            #to check if user is a member in a specific shop and not just any shop
            member = get_object_or_404(Member,user=request.user, shop=shop)
            return member.member_type in ['admin', 'owner']

        except Member.DoesNotExist:
            raise NotFound(detail="request.user is not a member of this shop")


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        shop_uuid = view.kwargs.get('uuid')
        try:
            shop = get_object_or_404(Shop, uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")
        try:
            #to check if user is a member in a specific shop and not just any shop
            member = get_object_or_404(Member,user=request.user, shop=shop)
            return member.member_type in ['manager','admin', 'owner']

        except Member.DoesNotExist:
            raise NotFound(detail="request.user is not a member of this shop")


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        shop_uuid = view.kwargs.get('uuid')
        try:
            shop = get_object_or_404(Shop, uuid=shop_uuid)
        except Shop.DoesNotExist:
            raise NotFound(detail="Shop does not exist")
        try:
            #to check if user is a member in a specific shop and not just any shop
            member = get_object_or_404(Member,user=request.user, shop=shop)
            return member.member_type in ['staff','manager','admin', 'owner']

        except Member.DoesNotExist:
            raise NotFound(detail="request.user is not a member of this shop")







