from django.forms import ModelForm

from apps.models import Type_PSL


class TypepslForm(ModelForm):
    class Meta:
        model = Type_PSL
        fields = '__all__'
