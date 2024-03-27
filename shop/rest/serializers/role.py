from shop.models import Role
from rest_framework import serializers

from common.helper import get_attribute

class RoleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    shop_name = serializers.SerializerMethodField()
    user_uuid = serializers.SerializerMethodField()
    shop_uuid = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = ['uuid','user','shop', 'user_uuid', 'username', 'phone_number', 'shop_uuid', 'shop_name', 'role_type']
        read_only_fields = ['uuid']

    def get_user_uuid(self, instance):
        return get_attribute(instance, 'user', 'uuid')

    def get_username(self, instance):
        return get_attribute(instance, 'user', 'username')

    def get_phone_number(self, instance):
        return get_attribute(instance, 'user', 'phone_number')

    def get_shop_uuid(self, instance):
        return get_attribute(instance, 'shop', 'uuid')

    def get_shop_name(self, instance):
        return get_attribute(instance, 'shop', 'name')

