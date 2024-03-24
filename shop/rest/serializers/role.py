from shop.models import Role
from rest_framework import serializers

class RoleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    class Meta:
        model = Role
        fields = ['user', 'username', 'phone_number', 'shop', 'role_type']

    def get_username(self, role_instance):
        # If the role_instance is a single instance
        if hasattr(role_instance, 'user'):
            return role_instance.user.username
        # If the role_instance is a queryset of instances
        elif hasattr(role_instance, 'first') and hasattr(role_instance.first(), 'user'):
            return [role.user.username for role in role_instance]

    def get_phone_number(self, role_instance):
        # If the role_instance is a single instance
        if hasattr(role_instance, 'user'):
            return role_instance.user.phone_number
        # If the role_instance is a queryset of instances
        elif hasattr(role_instance, 'first') and hasattr(role_instance.first(), 'user'):
            return [role.user.phone_number for role in role_instance]

