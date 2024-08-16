from rest_framework import pagination
from rest_framework.response import Response


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