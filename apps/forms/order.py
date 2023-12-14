from django.forms import ModelForm

from apps.models.order import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update({'class':'form-control', 'placeholder':'Client'})
        self.fields['quantity'].widget.attrs.update({'class':'form-control', 'placeholder':'Quantité'})
