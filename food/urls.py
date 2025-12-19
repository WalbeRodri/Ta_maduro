from rest_framework import routers
from .views import FoodView, FoodDetailView
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'foods', FoodView, basename='foods')

urlpatterns = [
    path('', include(router.urls)),
    path('food/<int:id>/', FoodDetailView.as_view(), name='food_detail'),
]
