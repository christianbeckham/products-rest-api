from rest_framework import serializers
from .models import Review

# Create your serializers here.


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review_text', 'rating', 'name', 'product']
