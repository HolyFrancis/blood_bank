from django.db import models

from apps.models.donor import Donor

class Medication(models.Model):
    name = models.CharField(max_length=255)
    donor = models.ManyToManyField(Donor)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)