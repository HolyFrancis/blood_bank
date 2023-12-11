from django.forms import ModelForm

from apps.models import EquipmentType


class EquipmentTypeForm(ModelForm):
    class Meta:
        model = EquipmentType
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form_control", "placeholder": "Nom"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Description"}
        )
