from django.forms import ModelForm

from apps.models import Blood_analysis


class BloodAnalysisForm(ModelForm):
    class Meta:
        model = Blood_analysis
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["analysis"].widget.attrs.update(
            {"class": "form-select"}
        )
        self.fields["blood"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )
        self.fields["result"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Résultat"}
        )
