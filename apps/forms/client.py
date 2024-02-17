from django.forms import ModelForm

from apps.models.client import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder':'Nom'})
        self.fields['phone'].widget.attrs.update({'class':'form-control', 'placeholder':'Téléphone'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'E-mail'})
        self.fields['adress'].widget.attrs.update({'class':'form-control', 'placeholder':'Adresse'})
        self.fields['password'].widget.attrs.update({'class':'form-control', 'placeholder':'Mot de Passe'})
