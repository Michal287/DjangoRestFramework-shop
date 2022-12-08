from ..models import Product
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist


class CartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=False)

    def validate(self, data):
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        try:
            product = Product.objects.get(pk=product_id)

            if product.quantity < quantity:
                raise serializers.ValidationError('There is not enough product available')

        except ObjectDoesNotExist:
            raise serializers.ValidationError('Product not exist')

        return data
