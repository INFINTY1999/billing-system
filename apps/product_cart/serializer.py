from rest_framework import serializers
from .models import CartItem
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "product_title", "category"]


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = CartItem
        fields = ["id", "quantity", "product"]
