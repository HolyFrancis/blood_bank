from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    ROLES = (("Admin", "Admin"), ("Client", "Client"), ("Docteur", "Docteur"), ("Gestionnaire", "Gestionnaire"), ("Laborantin", "Laborantin"), ("Infirmier(e)", "Infirmier(e)"))
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=20, null=True, blank=False, choices=ROLES)
    donor = models.ForeignKey("Donor", on_delete=models.CASCADE, null=True, blank=True, related_name="users", related_query_name="user")

    @property
    def is_donor(self):
        if self.donor:
            return True
        else:
            return False
