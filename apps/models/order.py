from django.db import models

from apps.models.client import Client

class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=False, blank=False,default=0)
    updated = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)