from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from store.models import Product


class ProductSerializer(ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=6)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'collection']

