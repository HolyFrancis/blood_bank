from django.db import models

from apps.models.donor import Donor

class Surgery(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    donor = models.ManyToManyField(Donor)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)