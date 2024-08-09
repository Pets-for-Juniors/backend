from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, pagination, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Animals
from .serializers import AnimalSerializer, AnimalListSerializer


# Create your views here.

class AnimalAPIView(mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer


class CustomPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        queryset = Animals.objects.all()
        return Response({
            'count': queryset.count(),
            'data': data
        })


class AnimalListAPIView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Animals.objects.all()
    serializer_class = AnimalListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = CustomPagination
    filterset_fields = '__all__'

