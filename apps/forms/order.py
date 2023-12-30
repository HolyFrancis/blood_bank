from django.forms import ModelForm

from apps.models.order import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["client"].widget.attrs.update({"class": "form-control"})
        self.fields["type_psl"].widget.attrs.update({"class": "form-control"})
        # self.fields['quantity'].widget.attrs.update({'class':'form-control', 'placeholder':'Quantité'})
        self.fields["quantity_A_plus"].widget.attrs.update({"class": "form-control", "placeholder": "Quantité pour le groupe sanguin A+"})
        self.fields["quantity_A_m"].widget.attrs.update({"class": "form-control", "placeholder": "Quantité pour le groupe sanguin A-"})
        self.fields["quantity_B_plus"].widget.attrs.update({"class": "form-control", "placeholder": "Quantité pour le groupe sanguin B+"})
        self.fields["quantity_B_m"].widget.attrs.update({"class": "form-control", "placeholder": "Quantité pour le groupe sanguin B-"})
        self.fields["quantity_AB_plus"].widget.attrs.update({"class": "form-control", "placeholder": "Quantité pour le groupe sanguin AB+"})
        self.fields["quantity_AB_m"].widget.attrs.update({"class": "form-control", "placeholder": "Quantité pour le groupe sanguin AB-"})
        self.fields["quantity_O_plus"].widget.attrs.update({"class": "form-control", "placeholder": "Quantité pour le groupe sanguin O+"})
        self.fields["quantity_O_m"].widget.attrs.update({"class": "form-control", "placeholder": "Quantité pour le groupe sanguin O-"})
        self.fields["status"].widget.attrs.update({"class": "form-control", "placeholder": "Status"})
