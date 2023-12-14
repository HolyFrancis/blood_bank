from django.forms import ModelForm

from apps.models.location import Location

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder':'Nom'})
        self.fields['stock'].widget.attrs.update({'class':'form-control', 'placeholder':'Stock'})
