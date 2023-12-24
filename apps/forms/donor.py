from django.forms import ModelForm

from apps.models.donor import Donor

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Nom'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Prénom(s)'})
        self.fields['cni'].widget.attrs.update({'class':'form-control', 'placeholder':'CNI'})
        self.fields['weight'].widget.attrs.update({'class':'form-control', 'placeholder':'Poids'})
        self.fields['sex'].widget.attrs.update({'class':'form-select'})
        self.fields['blood_group'].widget.attrs.update({'class':'form-select'})
        self.fields['last_donation'].widget.attrs.update({'class':'form-check-input'})
        self.fields['drugs'].widget.attrs.update({'class':'form-check-input'})
        self.fields['tattoo_piercing'].widget.attrs.update({'class':'form-check-input'})
        self.fields['disease'].widget.attrs.update({'class':'form-check-input'})
        self.fields['surgery'].widget.attrs.update({'class':'form-check-input'})
        self.fields['under_medication'].widget.attrs.update({'class':'form-check-input'})
        self.fields['vaccine'].widget.attrs.update({'class':'form-check-input'})
        self.fields['dentist'].widget.attrs.update({'class':'form-check-input'})
        self.fields['pregnancy'].widget.attrs.update({'class':'form-check-input'})
        self.fields['transfusion'].widget.attrs.update({'class':'form-check-input'})
        self.fields['anemia'].widget.attrs.update({'class':'form-check-input'})
        self.fields['infections'].widget.attrs.update({'class':'form-check-input'})
        self.fields['examens'].widget.attrs.update({'class':'form-check-input'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['phone'].widget.attrs.update({'class':'form-control', 'placeholder':'Numéro de Téléphone'})
        self.fields['status'].widget.attrs.update({'class':'form-select', 'placeholder':'Adresse mail'})