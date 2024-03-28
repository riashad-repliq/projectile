from common.helper import DynamicFieldsModelSerializer

from core.models import User
from shop.models import Shop, Member
from rest_framework import serializers
from shop.rest.serializers.member import MemberSerializer

class ShopSerializer(DynamicFieldsModelSerializer):
    members = MemberSerializer(many=True, read_only =True, fields=('uuid', 'user_uuid', 'username', ))

    class Meta:
        model = Shop
        fields = ['uuid', 'name', 'location', 'members']
        read_only_fields = ['uuid']
