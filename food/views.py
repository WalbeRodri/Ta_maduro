from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import FoodItemSerializer
from .models import FoodItem

class FoodView(viewsets.ModelViewSet):            
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()

class FoodDetailView(View):
    def get(self, request, id):
        food_item = FoodItem.objects.get(id=id)
        context = {'food_item': food_item}
        return render(request, 'food/food_detail.html', context)