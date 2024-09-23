from .models import Animals, TypeAnimals
from .constans import age_data
from pets_for_juniors.utils import BasePaginationView


class BreedPagination(BasePaginationView):
    queryset = Animals.objects.values('breed', 'type').distinct()


# class GenderPagination(BasePaginationView):
#     queryset = Animals.objects.values('sex').distinct()


class TypePagination(BasePaginationView):
    queryset = TypeAnimals.objects.all()


class CustomPagination(BasePaginationView):
    queryset = Animals.objects.all()


# class AgePagination(BasePaginationView):
#     queryset = age_data