from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from .models import People
from .serializers import PeopleSerializer
from pets_for_juniors.utils import ForPagination


class PeoplePagination(ForPagination):
    queryset = People.objects.all()


class PeopleAPIView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'age', 'job_title', 'about_person', 'id']
    pagination_class = PeoplePagination
