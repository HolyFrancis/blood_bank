from django.forms import ModelForm

from apps.models import PSL


class PslForm(ModelForm):
    class Meta:
        model = PSL
        fields = '__all__'