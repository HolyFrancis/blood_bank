from collections.abc import Mapping
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList

from apps.models.donor import Donor

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Last Name'})
        self.fields['cni'].widget.attrs.update({'class':'form-control', 'placeholder':'ID Card'})
        self.fields['weight'].widget.attrs.update({'class':'form-control', 'placeholder':'Weight'})
        self.fields['parteners'].widget.attrs.update({'class':'form-control', 'placeholder':'Number of Partners'})
        # self.fields['birthday'].widget.attrs.update({'class':'form-control'})
        self.fields['sex'].widget.attrs.update({'class':'form-select'})
        self.fields['blood_group'].widget.attrs.update({'class':'form-select'})
        # self.fields['last_donation'].widget.attrs.update({'data-provide':"datepicker", 'class':'form-control'})
        self.fields['drugs'].widget.attrs.update({'class':'form-check-input'})
        self.fields['tattoo'].widget.attrs.update({'class':'form-check-input'})
        self.fields['piercing'].widget.attrs.update({'class':'form-check-input'})
        self.fields['has_disease'].widget.attrs.update({'class':'form-check-input'})
        self.fields['had_surgery'].widget.attrs.update({'class':'form-check-input'})
        self.fields['under_medication'].widget.attrs.update({'class':'form-check-input'})