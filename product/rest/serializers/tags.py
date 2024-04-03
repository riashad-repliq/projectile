from rest_framework import serializers

from product.models import Tag, TaggedProduct

from common.helper import DynamicFieldsModelSerializer

class TagSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Tag
        fields =['name']


