from django.db import models

from apps.models.order import Order

class Bill(models.Model):
    amount = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)