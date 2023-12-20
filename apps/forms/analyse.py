from django.forms import ModelForm

from apps.models import Analysis

class AnalysisForm(ModelForm):
    class Meta:
        model = Analysis
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['result'].widget.attrs.update({'class':'form-select'})