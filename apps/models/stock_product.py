from django.db import models

from apps.models.stock import Stock
from apps.models.product import Product

class Stock_product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)