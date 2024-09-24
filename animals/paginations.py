from rest_framework import pagination

from .models import Animals, TypeAnimals, AgeAnimals, Gender, Breed



class TypePagination(pagination.LimitOffsetPagination):
    queryset = TypeAnimals.objects.all()


class CustomPagination(pagination.LimitOffsetPagination):
    queryset = Animals.objects.all()


class AgePagination(pagination.LimitOffsetPagination):
    queryset = AgeAnimals.objects.all()


class GenderPagination(pagination.LimitOffsetPagination):
    queryset = Gender.objects.all()


class BreedPagination(pagination.LimitOffsetPagination):
    queryset = Breed.objects.all()
