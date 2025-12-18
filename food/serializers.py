from rest_framework import serializers
from .models import FoodType, FoodItem

class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['id', 'type']

class FoodItemSerializer(serializers.ModelSerializer):
    type = FoodTypeSerializer()
    
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'description', 'price', 'image_good', 'image_bad', 'how_to_analyze', 'type']