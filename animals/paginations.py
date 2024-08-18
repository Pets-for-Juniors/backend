from .models import Animals
from .constans import age_data
from pets_for_juniors.utils import BasePaginationView


class BreedPagination(BasePaginationView):
    queryset = Animals.objects.values('breed', 'type').distinct()


class GenderPagination(BasePaginationView):
    queryset = Animals.objects.values('sex').distinct()


class TypePagination(BasePaginationView):
    queryset = Animals.objects.values('type').distinct()


class CustomPagination(BasePaginationView):
    queryset = Animals.objects.all()


class AgePagination(BasePaginationView):
    queryset = age_data