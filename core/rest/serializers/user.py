from django.contrib.auth import get_user_model

from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer


from shop.rest.serializers.member import ManageMemberSerializer

from cart.models import Cart

class UserSerializer(DynamicFieldsModelSerializer):#shop info not found
    associated_shops = ManageMemberSerializer(many=True, fields=('member_type', 'shop_name'), source='member_set' , read_only = True,)

    class Meta:
        model = get_user_model()
        fields = ['uuid', 'phone_number', 'username', 'password', 'associated_shops']

        write_only_fields = ['password']
        read_only_fields = ['uuid']


    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Cart.objects.create(user=user)

        return user

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     password = validated_data.get('password', instance.password)
    #     user = super().update(instance, validated_data)
    #     return user

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    def validate(self, data):
        if len(data['password']) < 5:
            raise serializers.ValidationError("Password must be at least 5 characters")
        return data
