from django_filters import NumberFilter, FilterSet

from .models import Animals


class AnimalFilter(FilterSet):
    age__gte = NumberFilter(field_name='age', lookup_expr='gte')
    age__lte = NumberFilter(field_name='age', lookup_expr='lte')

    class Meta:
        model = Animals
        fields = '__all__'
