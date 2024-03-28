from shop.models import Member
from rest_framework import serializers

from common.helper import get_attribute,DynamicFieldsModelSerializer
from core.rest.serializers import user

class MemberSerializer(DynamicFieldsModelSerializer):
    user_info = serializers.SerializerMethodField()
    shop_info= serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ['uuid', 'member_type', 'user_info', 'shop_info']
        read_only_fields = ['uuid']

    def get_user_info(self, obj):
        user = obj.user
        return {
            'username': user.username,
            'phone_number': user.phone_number,
            'uuid': user.uuid
        }

    def get_shop_info(self, obj):
        shop = obj.shop
        return {
            'uuid': shop.uuid,
            'shop_name': shop.name,
            'location': shop.location,

        }

