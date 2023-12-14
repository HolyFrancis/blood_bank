from django.forms import ModelForm

from apps.models.stock import Stock

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder':'Nom'})
