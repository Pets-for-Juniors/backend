from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, filters, pagination
from .models import People
from .serializers import PeopleSerializer


class PeoplePagination(pagination.LimitOffsetPagination):
    queryset = People.objects.all()


class PeopleAPIView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'age', 'job_title', 'about_person', 'id']
    pagination_class = PeoplePagination
