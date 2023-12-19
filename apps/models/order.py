from django.db import models

from apps.models.client import Client
from apps.models.type_psl import Type_PSL

class Order(models.Model):
    STATUS = (("En Attente", "En Attente"),("Délivrée","Délivrée"),("Annulée","Annulée"))
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type_psl = models.ForeignKey(Type_PSL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0])
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)