from django.forms import ModelForm

from apps.models import Solution


class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Nom"}
        )
        self.fields["duration"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Durée"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Description"}
        )
