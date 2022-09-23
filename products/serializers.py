from rest_framework import serializers
from .models import Product

# Create your serializers here.


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description',
                  'price', 'inventory_quantity', 'image_url']
