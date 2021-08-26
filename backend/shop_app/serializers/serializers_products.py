from ..models import Product, Category, Image, Order
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['product', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(required=False, many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'quantity', 'price', 'category', 'images']

    def create(self, validated_data):
        product = super().create(validated_data)

        images = self.context['request'].FILES.getlist('images')

        for image in images:
            image_object = Image(product=product, image=image)
            image_object.save()

        return product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
