from django.forms import ModelForm

from apps.models import Analysis

class AnalysisForm(ModelForm):
    class Meta:
        model = Analysis
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['irregular_antibodies'].widget.attrs.update({'class':'form-select'})
        self.fields['hiv_test'].widget.attrs.update({'class':'form-select'})
        self.fields['hepatites_test'].widget.attrs.update({'class':'form-select'})
        self.fields['anti_hlv1_test'].widget.attrs.update({'class':'form-select'})
        self.fields['anti_hlv2_test'].widget.attrs.update({'class':'form-select'})
        self.fields['malaria_test'].widget.attrs.update({'class':'form-select'})
        self.fields['result'].widget.attrs.update({'class':'form-select'})