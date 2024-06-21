from django.urls import path
from .views import FoodList, Food

urlpatterns = [
    path('foods/', FoodList.as_view()),
    path('foods/<int:pk>', Food.as_view())
]