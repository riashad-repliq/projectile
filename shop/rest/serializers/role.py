from shop.models import Role
from rest_framework import serializers

def get_attribute(instance, model, attribute):
    if hasattr(instance, model):
        return getattr(getattr(instance, model), attribute, None)

class RoleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    shop_name = serializers.SerializerMethodField()
    class Meta:
        model = Role
        fields = ['user', 'username', 'phone_number', 'shop', 'shop_name', 'role_type']

    def get_username(self, instance):
        return get_attribute(instance, 'user', 'username')

    def get_phone_number(self, instance):
        return get_attribute(instance, 'user', 'phone_number')

    def get_shop_name(self, instance):
        return get_attribute(instance, 'shop', 'name')

