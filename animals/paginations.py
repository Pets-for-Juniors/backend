import sys

from rest_framework import pagination
from rest_framework.response import Response

from .models import Animals


class GenderPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        queryset = Animals.objects.values('sex').distinct()
        return Response({
            'count': queryset.count(),
            'data': data
        })


class CustomPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        queryset = Animals.objects.all()
        return Response({
            'count': queryset.count(),
            'data': data
        })


class TypePagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        queryset = Animals.objects.values('type').distinct()
        return Response({
            'count': queryset.count(),
            'data': data
        })


class BreedPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        queryset = Animals.objects.values('breed', 'type').distinct()
        return Response({
            'count': queryset.count(),
            'data': data
        })


class AgePagination(pagination.LimitOffsetPagination):

    def get_paginated_response(self, data):
        age_data = [
            {'title': "Молодые", 'minAge': 0, 'maxAge': 2},
            {'title': "В самом расцвете сил", 'minAge': 3, 'maxAge': 6},
            {'title': "Пожилые", 'minAge': 7, 'maxAge': sys.maxsize}
        ]

        return Response({
            'count': len(age_data),
            'data': data
        })
