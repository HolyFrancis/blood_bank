from django.forms import ModelForm

from apps.models import PSL


class PslForm(ModelForm):
    class Meta:
        model = PSL
        fields = '__all__'

class GRForm(ModelForm):
    class Meta:
        model = PSL
        fields = '__all__'


class PFCForm(ModelForm):
    class Meta:
        model = PSL
        exclude = ['solution']

class CPSForm(ModelForm):
    class Meta:
        model = PSL
        exclude = ['solution']
        
class CPSPartialForm(ModelForm):
    class Meta:
        model = PSL
        exclude = ['serial', 'solution']