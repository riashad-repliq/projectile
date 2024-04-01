from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
from shop.models import Shop, Member
from rest_framework import serializers

from common.helper import  DynamicFieldsModelSerializer

User = get_user_model()


class ListCreateMemberSerializer(DynamicFieldsModelSerializer):
    user_uuid = serializers.UUIDField(write_only=True)
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ['uuid', 'member_type', 'user_uuid',  'user_info']
        read_only_fields = ['uuid']

    def create(self, validated_data):
        user_uuid = validated_data.pop('user_uuid')
        user = get_object_or_404(User, uuid=user_uuid)

        member = Member.objects.create(user=user,**validated_data)
        return member

    def get_user_info(self, obj):
        user = obj.user
        return {
            'username': user.username,
            'phone_number': user.phone_number,
            'uuid': user.uuid
        }


class ManageMemberSerializer(DynamicFieldsModelSerializer):
    shop_name = serializers.CharField(source='shop.name')

    class Meta:
        model = Member
        fields = ['uuid', 'shop_name', 'member_type']
        read_only_fields = ['uuid']


8