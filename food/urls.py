from rest_framework import routers
from .views import FoodView
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'foods', FoodView, basename='foods')

urlpatterns = [
    path('', include(router.urls)),
]
