from rest_framework import serializers


from common.helper import DynamicFieldsModelSerializer

from product.models import Product, Image, Tag
from product.rest.serializers.image import ImageSerializer
from product.rest.serializers.tags import TagSerializer

"""Public Product Serializers"""
class ProductSerializer(DynamicFieldsModelSerializer):
    images = ImageSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = ['uuid','slug', 'name', 'description', 'price','product_profile_image', 'quantity', 'images' ]



"""Private Product Serializers"""

class ListCreateProductSerializer(DynamicFieldsModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False, write_only= True)

    class Meta:
        model = Product
        fields = ['uuid', 'name', 'description', 'price', 'product_profile_image', 'quantity', 'images', 'tags']

    def tags(self, tags, product):
        """Handle getting or creating tags as needed."""
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(**tag)
            product.tags.add(tag_obj)

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        tags = validated_data.pop('tags', [])


        product = Product.objects.create(**validated_data)
        self.tags(tags, product)
        for image in images:
            Image.objects.create(product=product, image=image)

        return product


# class ManageProductSerializer(DynamicFieldsModelSerializer):
#     images = ImageSerializer(many=True, required=False)
#     class Meta:
#         model = Product
#         fields = ['uuid', 'name', 'description', 'product_profile_image','price', 'quantity', 'images']

class ManageProductSerializer(DynamicFieldsModelSerializer):
    images = ImageSerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['uuid', 'name', 'description', 'product_profile_image', 'price', 'quantity', 'tags' ,'images']

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        images_serializer = self.fields['images']

        # Update product fields
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Update or create images
        for image_data in images_data:
            image_id = image_data.get('id', None)
            if image_id:
                image_instance = instance.images.filter(id=image_id).first()
                if image_instance:
                    images_serializer.update(image_instance, image_data)
            else:
                image_data['product'] = instance.id
                images_serializer.create(image_data)

        return instance
