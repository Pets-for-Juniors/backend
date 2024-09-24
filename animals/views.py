from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .filters import AnimalFilter
from .models import Animals, TypeAnimals, AgeAnimals, Gender, Breed
from .paginations import AgePagination, TypePagination, CustomPagination, GenderPagination, BreedPagination
from .serializers import (AnimalSerializer, AnimalListSerializer, TypeFilterSerializer, AgeFilterSerializer,
                          GenderFilterSerializer, BreedFilterSerializer)


# Create your views here.
class AnimalAPIView(mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer


class AnimalListAPIView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Animals.objects.all()
    serializer_class = AnimalListSerializer
    filterset_class = AnimalFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = CustomPagination


class TypeFilterAPIView(ListAPIView):
    queryset = TypeAnimals.objects.all()
    serializer_class = TypeFilterSerializer
    pagination_class = TypePagination
    filterset_fields = '__all__'


class AgeFilterAPIView(ListAPIView):
    queryset = AgeAnimals.objects.all()
    serializer_class = AgeFilterSerializer
    pagination_class = AgePagination
    filterset_fields = '__all__'


class GenderFilterAPIView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Gender.objects.all()
    serializer_class = GenderFilterSerializer
    pagination_class = GenderPagination
    filterset_fields = '__all__'


class BreedFilterAPIView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Breed.objects.all()
    serializer_class = BreedFilterSerializer
    pagination_class = BreedPagination
    filterset_fields = '__all__'