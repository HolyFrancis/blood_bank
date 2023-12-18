from django.forms import ModelForm

from apps.models import PSL, Price


class PslForm(ModelForm):
    class Meta:
        model = PSL
        fields = ['serial', 'typ', 'volume', 'solution', 'blood', 'duration']


class PriceForm(ModelForm):
    class Meta:
        model = Price
        fields = "__all__"