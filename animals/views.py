import sys


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, filters
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Animals
from .paginations import GenderPagination, CustomPagination, TypePagination, BreedPagination, AgePagination
from .serializers import AnimalSerializer, AnimalListSerializer, BreedSerializer, TypeSerializer, GenderSerializer, \
    AgeSerializer
from .constans import age_data


# Create your views here.

class AnimalAPIView(mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer


class AnimalListAPIView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Animals.objects.all()
    serializer_class = AnimalListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = CustomPagination
    filterset_fields = '__all__'


class GenderAPIView(generics.ListAPIView):
    queryset = Animals.objects.values('sex').distinct()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sex']
    serializer_class = GenderSerializer
    pagination_class = GenderPagination


class AgeAPIView(generics.ListAPIView):
    serializer_class = AgeSerializer
    pagination_class = AgePagination

    def get_queryset(self):
        global age_data

        title = self.request.query_params.get('title')
        min_age = self.request.query_params.get('minAge')
        max_age = self.request.query_params.get('maxAge')

        if title:
            age_data = [item for item in age_data if item['title'] == title]
        if min_age:
            age_data = [item for item in age_data if item['minAge'] >= int(min_age)]
        if max_age:
            age_data = [item for item in age_data if item['maxAge'] <= int(max_age)]

        return age_data

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class TypeAPIView(generics.ListAPIView):
    queryset = Animals.objects.values('type').distinct()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    serializer_class = TypeSerializer
    pagination_class = TypePagination


class BreedAPIView(generics.ListAPIView):
    queryset = Animals.objects.values('breed', 'type').distinct()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['breed', 'type']
    serializer_class = BreedSerializer
    pagination_class = BreedPagination
