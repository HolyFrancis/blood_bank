from django.db import models

from apps.models.stock import Stock

class Location(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    stock = models.ManyToManyField(Stock)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)