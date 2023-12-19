from django.forms import ModelForm

from apps.models.order import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update({'class':'form-control'})
        self.fields['type_psl'].widget.attrs.update({'class':'form-control'})
        self.fields['quantity'].widget.attrs.update({'class':'form-control', 'placeholder':'Quantité'})
        self.fields['status'].widget.attrs.update({'class':'form-control', 'placeholder':'Status'})