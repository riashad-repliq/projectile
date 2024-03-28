from rest_framework import permissions
from shop.models import Member
class ShopPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                member= Member.objects.filter(user=request.user)
                print (member)
                member_type = member.member_type
                if member_type in ['owner', 'admin', 'manager']:
                    return True
            except Member.DoesNotExist:
                pass
        return False