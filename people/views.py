from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import People
from .serializers import PeopleSerializer


class PeoplePagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 1
    def get_paginated_response(self, data):
        queryset = People.objects.all()
        return Response({
            'count': queryset.count(),
            'data': data
        })


class PeopleAPIView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'age', 'job_title', 'about_person', 'id']
    pagination_class = PeoplePagination
