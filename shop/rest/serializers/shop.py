from shop.models import Shop, Role
from rest_framework import serializers

class RoleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Role
        fields = ['user', 'username', 'shop', 'role_type']

    def get_username(self, role_instance):
        # If the role_instance is a single instance
        if hasattr(role_instance, 'user'):
            return role_instance.user.username
        # If the role_instance is a queryset of instances
        elif hasattr(role_instance, 'first') and hasattr(role_instance.first(), 'user'):
            return [role.user.username for role in role_instance]
class ShopSerializer(serializers.ModelSerializer):
    roles_field = RoleSerializer(many=True, source='roles')

    class Meta:
        model = Shop
        fields = ['id', 'name', 'location', 'roles_field']

