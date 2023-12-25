from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    ROLES = (
        ('Admin','Admin'), 
        ('Client','Client'),
        ('Docteur','Docteur'),
        ('Gestionnaire','Gestionnaire'),
        ('Laborantin','Laborantin'),
        ('Infirmier(e)','Infirmier(e)')
        )
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=20, null=True, blank=False, choices=ROLES)
