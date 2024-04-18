from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FoodSerializer
from .models import Food
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class FoodView(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset =  Food.objects.all()

@api_view(['GET'])
def hello(request):
    
    return Response({'message' : 'Hello world'})