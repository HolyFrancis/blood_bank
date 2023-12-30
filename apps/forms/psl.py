from django import forms
from django.forms import ModelForm

from apps.models import PSL


class PslForm(ModelForm):
    class Meta:
        model = PSL
        fields = '__all__'
        
class SerialForm(forms.Form):
    serial = forms.CharField(max_length=50, required=True)