from django.forms import ModelForm

from apps.models import Reactant


class ReactantForm(ModelForm):
    class Meta:
        model = Reactant
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form_control", "placeholder": "Nom"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Description"}
        )
