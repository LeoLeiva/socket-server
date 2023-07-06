from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    code = serializers.UUIDField(required=True)
    price_buy = serializers.DecimalField(max_digits=30, decimal_places=2)
    price_sell = serializers.DecimalField(max_digits=30, decimal_places=2)
    description = serializers.CharField(max_length=250, required=False)
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')

    class Meta:
        model = Product
        fields = (
            'code',
            'price_buy',
            'price_sell',
            'description',
            'created_at',
            'updated_at'
        )
