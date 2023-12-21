import django_filters

from apps.models import PSL

class PSLFilter(django_filters.FilterSet):
    class Meta:
        model = PSL
        fields = ["type_psl", "solution"]