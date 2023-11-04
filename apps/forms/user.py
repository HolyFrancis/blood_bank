from django.forms import ModelForm

from apps.models import Users


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]
