from django.forms import ModelForm

from apps.models import Analysis

class AnalysisForm(ModelForm):
    class Meta:
        model = Analysis
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['typ'].widget.attrs.update({'class':'form-control', 'placeholder':'Type'})
        self.fields['equipment'].widget.attrs.update({'class':'form-control', 'placeholder':'Equipement'})