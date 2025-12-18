from django.contrib import admin
from .models import FoodType, FoodItem

# Register your models here.
@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'price')