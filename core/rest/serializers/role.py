from rest_framework import serializers

from common.helper import get_attribute
from shop.rest.serializers.role import RoleSerializer
from shop.models import Role


class UserRoleSerializer(RoleSerializer):
    role_uuid = serializers.SerializerMethodField()
    shop_uuid = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = ['role_uuid', 'shop_uuid', 'role_type']
        read_only_fields = ['uuid','shop_uuid']


    def get_shop_uuid(self, instance):
        return get_attribute(instance, 'shop', 'uuid')

    def get_role_uuid(self, instance):
        return instance.uuid