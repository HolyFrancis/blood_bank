import django_filters

from apps.models import Analysis

class AnalysisFilter(django_filters.FilterSet):
    class Meta:
        model = Analysis
        fields = ["result"]