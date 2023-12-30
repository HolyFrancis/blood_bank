import django_filters
from django_filters import CharFilter

from apps.models import Donor

class DonorFilter(django_filters.FilterSet):
    class Meta:
        model = Donor
        fields = ["blood_group", "status"]