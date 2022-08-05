

import django_filters
from .models import *

class VaccinFilter(django_filters.FilterSet):
    class Meta:
        model = Vaccination 
        fields = '__all__'

    