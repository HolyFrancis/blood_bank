from django.forms import ModelForm

from apps.models import PSL


class PslForm(ModelForm):
    class Meta:
        model = PSL
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["serial"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Serial"}
            )
            self.fields["volume"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Volume"}
            )
            self.fields["start_date"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Sample"}
            )
            self.fields["end_date"].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )
            self.fields["type_psl"].widget.attrs.update({"class": "form-select"})
            self.fields["blood"].widget.attrs.update(
                {"class": "form-select"}, "multiple"
            )
            self.fields["order"].widget.attrs.update({"class": "form-select"})
