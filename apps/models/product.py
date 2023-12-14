from django.db import models

from apps.models.psl import PSL
from apps.models.productType import ProductType

class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=False, blank=False)
    psl = models.ForeignKey(PSL, on_delete=models.CASCADE, null=True)
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)