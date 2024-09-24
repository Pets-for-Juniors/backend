from .models import Animals, TypeAnimals, AgeAnimals, Gender, Breed
from pets_for_juniors.utils import BasePaginationView


class TypePagination(BasePaginationView):
    queryset = TypeAnimals.objects.all()


class CustomPagination(BasePaginationView):
    queryset = Animals.objects.all()


class AgePagination(BasePaginationView):
    queryset = AgeAnimals.objects.all()


class GenderPagination(BasePaginationView):
    queryset = Gender.objects.all()


class BreedPagination(BasePaginationView):
    queryset = Breed.objects.all()
