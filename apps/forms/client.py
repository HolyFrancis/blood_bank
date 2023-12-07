
from collections.abc import Mapping
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList

from apps.models.client import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder':'Name'})
        self.fields['phone'].widget.attrs.update({'class':'form-control', 'placeholder':'Phone'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'E-mail'})
        self.fields['adress'].widget.attrs.update({'class':'form-control', 'placeholder':'Adress'})
