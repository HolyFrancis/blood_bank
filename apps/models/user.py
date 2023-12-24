from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True, blank=True)

