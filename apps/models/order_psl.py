from django.db import models

from apps.models.order import Order
from apps.models.psl import PSL

class Order_psl(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    psl = models.ForeignKey(PSL, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)