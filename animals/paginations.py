from .models import Animals
from .constans import age_data
from pets_for_juniors.utils import ForPagination


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