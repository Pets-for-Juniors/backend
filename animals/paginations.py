from rest_framework import pagination

from .models import Animals
from .constans import age_data


class BreedPagination(pagination.LimitOffsetPagination):
    queryset = Animals.objects.values('breed', 'type').distinct()


class GenderPagination(pagination.LimitOffsetPagination):
    queryset = Animals.objects.values('sex').distinct()


class TypePagination(pagination.LimitOffsetPagination):
    queryset = Animals.objects.values('type').distinct()


class CustomPagination(pagination.LimitOffsetPagination):
    queryset = Animals.objects.all()


class AgePagination(pagination.LimitOffsetPagination):
    queryset = age_data