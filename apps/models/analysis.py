from django.db import models

from apps.models import Product

class Analysis(models.Model):
    typ = models.CharField(max_length=255, null=False, blank=False)
    product = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)