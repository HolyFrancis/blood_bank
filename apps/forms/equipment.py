from django.forms import ModelForm

from apps.models import Equipment


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form_control", "placeholder": "Nom"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Description"}
        )
        self.fields["type_psl"].widget.attrs.update({"class": "form-select"})
        self.fields["equipmentType"].widget.attrs.update({"class": "form-select"})
