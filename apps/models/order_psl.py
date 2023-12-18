from django.db import models

from apps.models.order import Order
from apps.models.psl import PSL

class Order_psl(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=False, blank=False,default=0)
    updated = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    psl = models.ForeignKey(PSL, on_delete=models.CASCADE)