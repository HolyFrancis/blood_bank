from django.forms import ModelForm

from apps.models import Order_psl


class OrderpslForm(ModelForm):
    class Meta:
        model = Order_psl
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["quantity"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Résultat"}
        )
        self.fields["order"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )
        self.fields["psl"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )
