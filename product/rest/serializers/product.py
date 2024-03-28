from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from product.models import *

class ProductSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields= ['uuid']