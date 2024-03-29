from django.forms import ModelForm

from apps.models import Blood


class BloodForm(ModelForm):
    class Meta:
        model = Blood
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["serial"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Numéro de série"}
        )
        self.fields["volume"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )
        self.fields["sample"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Echantillon"}
        )
