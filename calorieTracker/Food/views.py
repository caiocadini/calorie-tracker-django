from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer
# Create your views here.

class FoodList(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

class Food(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

