from shop.rest.serializers.role import RoleSerializer
from shop.models import Role

class UserRoleSerializer(RoleSerializer):
    class Meta:
        model = Role
        fields = ['shop', 'role_type']
