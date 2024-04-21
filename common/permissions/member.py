from django.shortcuts import get_object_or_404

from rest_framework import permissions
from shop.models import Shop,Member
from common.permissions.helper import CustomGetObjectOr404

# class MemberPermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         shop_uuid = view.kwargs.get('shop_uuid')
#         shop =get_object_or_404(Shop,uuid=shop_uuid)


#         request_member = CustomGetObjectOr404.get_object_or_404(Member,user=request.user, shop=shop)

#         editable_member_uuid = view.kwargs.get('member_uuid')
#         editable_member = CustomGetObjectOr404.get_object_or_404(Member, uuid=editable_member_uuid)

#         if request_member.member_type == 'owner':
#             if editable_member.member_type == request_member.member_type:
#                 return request.method != 'DELETE'
#             elif editable_member.member_type == 'owner':
#                 return request.method == 'GET'
#             return True



#         elif request_member.member_type == 'staff':
#             return request.method == 'GET'


#         elif request_member.member_type == 'admin':
#             if editable_member.member_type in ['owner', 'admin']:
#                 return request.method == 'GET'

#             if request.method in ['POST', 'PATCH'] and 'member_type' in request.data:
#                 return request.data['member_type'] in ['manager', 'staff']

#             return request.method in ['GET', 'PUT', 'PATCH', 'POST']

#         elif request_member.member_type == 'manager':
#             if editable_member.member_type in ['owner', 'admin']:
#                 return False

#             if request.method in ['POST', 'PATCH'] and 'member_type' in request.data:
#                 return request.data['member_type'] in ['staff']

#             return request.method in ['GET', 'PUT', 'PATCH', 'POST']



class MemberPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        shop_uuid = view.kwargs.get('shop_uuid')
        shop =get_object_or_404(Shop,uuid=shop_uuid)

        member = CustomGetObjectOr404.get_object_or_404(Member,user=request.user, shop=shop)

        if member.member_type == 'owner':
            return True

        elif member.member_type == 'staff':
            return request.method == 'GET'

        elif member.member_type == 'admin':
            if request.method in ['POST', 'PATCH'] and 'member_type' in request.data:
                return request.data['member_type'] in ['manager', 'staff']

        elif member.member_type == 'manager':
            if request.method in ['POST', 'PATCH'] and 'member_type' in request.data:
                return request.data['member_type'] in ['staff']

        return request.method in ['GET', 'PUT', 'PATCH', 'POST']


# class MemberPermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         shop_uuid = view.kwargs.get('shop_uuid')
#         shop =get_object_or_404(Shop,uuid=shop_uuid)


#         request_member = CustomGetObjectOr404.get_object_or_404(Member,user=request.user, shop=shop)
#         if request.method == 'GET':
#             return True

#         if request.method == 'POST': #For ListCreate views
#             if request_member.member_type == 'owner':
#                return True

#             elif request_member.member_type == 'admin':
#                 if request.method == 'POST' and 'member_type' in request.data:
#                     return request.data['member_type'] in ['manager', 'staff']


#             elif request_member.member_type == 'manager':
#                 if request.method == 'POST' and 'member_type' in request.data:
#                     return request.data['member_type'] in ['staff']
#                 return True

#         if request_member.member_type == 'owner':
#             return True



#         elif request_member.member_type == 'staff':
#             return request.method == 'GET'


#         elif request_member.member_type == 'admin':

#             if request.method in ['POST', 'PATCH'] and 'member_type' in request.data:
#                 return request.data['member_type'] in ['manager', 'staff']

#             return request.method in ['GET', 'PUT', 'PATCH', 'POST']

#         elif request_member.member_type == 'manager':

#             if request.method in ['POST', 'PATCH'] and 'member_type' in request.data:
#                 return request.data['member_type'] in ['staff']

#             return request.method in ['GET', 'PUT', 'PATCH', 'POST']





#

# class MemberPermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         shop_uuid = view.kwargs.get('shop_uuid')
#         shop =get_object_or_404(Shop,uuid=shop_uuid)

#         request_member = CustomGetObjectOr404.get_object_or_404(Member,user=request.user, shop=shop)

#         if request.method in ['GET','POST']: #For ListCreate views

#             if request_member.member_type == 'owner':
#                 return True

#             elif request_member.member_type == 'staff':
#                 return request.method == 'GET'

#             elif request_member.member_type == 'admin':
#                 if request.method == 'POST' and 'member_type' in request.data:
#                     return request.data['member_type'] in ['manager', 'staff']

#                 return True

#             elif request_member.member_type == 'manager':
#                 if request.method == 'POST' and 'member_type' in request.data:
#                     return request.data['member_type'] in ['staff']
#                 return True



#         if request.method in ['PATCH', 'PUT', 'DELETE']: #For RetrieveUpdateDestroy views

#             editable_member_uuid = view.kwargs.get('member_uuid')
#             editable_member = CustomGetObjectOr404.get_object_or_404(Member, uuid=editable_member_uuid)

#             if editable_member.member_type == 'owner':
#                 if editable_member == request_member and request.method in ['PATCH', 'PUT']:
#                     return True
#                 return False

#             elif editable_member.member_type == 'admin':

#                 if request_member.member_type == 'owner':
#                     return True
#                 return False

#             elif editable_member.member_type == 'manager':

#                 if request_member.member_type in ['owner', 'admin']:
#                     if 'member_type' in request.data and 'member_type' in
#                 return False

#             elif editable_member.member_type == 'staff':

#                 if request_member.member_type in ['owner', 'admin', 'manager']:
#                     return True
#                 return False

class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # if request.method == 'POST'

class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.method == 'GET'
