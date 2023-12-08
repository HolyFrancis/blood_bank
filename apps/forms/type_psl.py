from django.forms import ModelForm

from apps.models import Type_psl


class Type_pslForm(ModelForm):
    class Meta:
        model = Type_psl
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["name"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Name"}
            )
            self.fields["duration"].widget.attrs.update({"class": "form-control"})
            self.fields["price"].widget.attrs.update(
                {"class": "form-control", "placeholder": "price"}
            )
            self.fields["description"].widget.attrs.update(
                {"class": "form-control", "placeholder": "description"}
            )
