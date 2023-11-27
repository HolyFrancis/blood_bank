from django.db import models

from apps.models.equipment import Equipment

class Analysis(models.Model):
    type = models.CharField(max_length=255, null=False, blank=False)
    equipment = models.ManyToManyField(Equipment)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)