from django.db import models

from apps.models.stock import Stock

class Location(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,null=True)
