from rest_framework import pagination
from rest_framework.response import Response


class BasePaginationView(pagination.LimitOffsetPagination):
    @staticmethod
    def get_counter(data):
        if data is not None:
            return len(data)

    def get_paginated_response(self, data):
        counter = self.get_counter(data)
        return Response({
            'count': counter,
            'data': data
        })