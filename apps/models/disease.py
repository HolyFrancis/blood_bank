from django.db import models

from apps.models.donor import Donor

class Disease(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    chronic = models.BooleanField(null=False, blank=False)
    autoimmune = models.BooleanField(null=False, blank=False)
    inflammatory = models.BooleanField(null=False, blank=False)
    donor = models.ManyToManyField(Donor)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)