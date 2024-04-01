from rest_framework import serializers

from product.models import Tag, TaggedShopProduct

from common.helper import DynamicFieldsModelSerializer

class TagSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Tag
        fields =['name']



class TaggedShopProductSerializer(DynamicFieldsModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = TaggedShopProduct
        fields = ['name']

    def get_name(self, obj):
        return obj.tag.name
