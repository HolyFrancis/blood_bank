from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm

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


class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = Users
        fields = ["old_password", "new_password1", "new_password2"]