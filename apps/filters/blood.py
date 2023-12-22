import django_filters

from apps.models import Blood

class BloodFilter(django_filters.FilterSet):
    class Meta:
        model = Blood
        fields = ["analysed", "state", "centrifuged"]