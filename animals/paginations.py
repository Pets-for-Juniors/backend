from rest_framework import pagination
from rest_framework.response import Response

from .models import Animals
from .constans import age_data


class ForPagination(pagination.LimitOffsetPagination):
    queryset = None

    def get_counter(self):
        if self.queryset is not None:
            return len(self.queryset)

    def get_paginated_response(self, data):
        counter = self.get_counter()
        return Response({
            'count': counter,
            'data': data
        })


class BreedPagination(ForPagination):
    queryset = Animals.objects.values('breed', 'type').distinct()


class GenderPagination(ForPagination):
    queryset = Animals.objects.values('sex').distinct()


class TypePagination(ForPagination):
    queryset = Animals.objects.values('type').distinct()


class CustomPagination(ForPagination):
    queryset = Animals.objects.all()


class AgePagination(ForPagination):
    queryset = age_data