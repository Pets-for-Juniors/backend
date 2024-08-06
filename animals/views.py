from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Animals
from .serializers import AnimalSerialiser



# Create your views here.

class AnimalAPIView(mixins.RetrieveModelMixin,
                   GenericViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerialiser










