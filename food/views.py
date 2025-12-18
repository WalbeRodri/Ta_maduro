from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FoodItemSerializer
from .models import FoodItem

class FoodView(viewsets.ModelViewSet):            
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()
