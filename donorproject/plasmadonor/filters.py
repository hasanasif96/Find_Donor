import django_filters

from .models import Donor

class DonorFilter(django_filters.FilterSet):
    class Meta:
        model= Donor
        fields=['city','age', 'Blood_Group' ]