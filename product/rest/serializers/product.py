from django.db.models import Avg

from rest_framework import serializers

from common.helper import DynamicFieldsModelSerializer

from product.models import Product, Image, Inventory, ProductInventory, CustomerReview
from product.rest.serializers.image import ImageSerializer

"""Public Product Serializers"""
class ProductSerializer(DynamicFieldsModelSerializer):
    images = ImageSerializer(many=True, required=False)
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['uuid','slug', 'name', 'description', 'price','product_profile_image','avg_rating', 'images' ]

    def get_avg_rating(self, obj):
        ratings = CustomerReview.objects.filter(product=obj)
        if ratings.exists():
            return ratings.aggregate(Avg('rating'))['rating__avg']
        return None


"""Private Product Serializers"""
class ProductInventorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ['quantity']

class ListCreateProductSerializer(DynamicFieldsModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=False)
    quantity = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = ['uuid', 'name', 'description', 'price', 'product_profile_image', 'images', 'quantity']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'quantity' not in data:
            try:
                product_inventory = ProductInventory.objects.get(product=instance)
                data['quantity'] = product_inventory.quantity
            except ProductInventory.DoesNotExist:
                data['quantity'] = None
        return data

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        quantity = validated_data.pop('quantity', None)
        product = Product.objects.create(**validated_data)
        shop = product.shop

        if quantity is not None:
            shop_inventory, _ = Inventory.objects.get_or_create(shop=shop)
            ProductInventory.objects.create(inventory=shop_inventory, product=product, quantity=quantity)

        else:
            raise serializers.ValidationError("A quantity must be specified")

        for image in images:
            Image.objects.create(product=product, image=image)

        return product



class ManageProductSerializer(DynamicFieldsModelSerializer):
    quantity = serializers.IntegerField(required=False)
    avg_rating = serializers.SerializerMethodField()
    # images = ImageSerializer(many=True, required=False, source='image_set')
    class Meta:
        model = Product
        fields = ['uuid', 'name', 'description', 'product_profile_image', 'price', 'quantity', 'avg_rating']

    def get_avg_rating(self, obj):
        ratings = CustomerReview.objects.filter(product=obj)
        if ratings.exists():
            return ratings.aggregate(Avg('rating'))['rating__avg']
        return None


    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'quantity' not in data:
            try:
                product_inventory = ProductInventory.objects.get(product=instance)
                data['quantity'] = product_inventory.quantity
            except ProductInventory.DoesNotExist:
                data['quantity'] = None
        return data

    def update(self, instance, validated_data):
        product_inventory = ProductInventory.objects.get(product=instance)
        quantity = validated_data.pop('quantity', product_inventory.quantity)
        # images_data = validated_data.pop('images', [])

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.product_profile_image = validated_data.get(
            'product_profile_image',
            instance.product_profile_image)
        instance.price = validated_data.get('price', instance.price)


        # for image_data in images_data:
        #     image_instance = Image.objects.filter(product=instance, id=image_data.get('id')).first()
        #     if image_instance:
        #         image_instance.image = image_data.get('image', image_instance.image)
        #         image_instance.save()
        #     else:
        #         Image.objects.create(product=instance, **image_data)

        instance.save()


        if quantity is not None:
            product_inventory, _ = ProductInventory.objects.get_or_create(product=instance)
            product_inventory.quantity = quantity
            product_inventory.save()
        else:
            raise serializers.ValidationError("A quantity must be specified")

        return instance
