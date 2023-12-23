from django.db import models

from apps.models.client import Client
from apps.models.type_psl import Type_PSL


class Order(models.Model):
    STATUS = (("En Attente", "En Attente"), ("Délivrée", "Délivrée"), ("Annulée", "Annulée"))
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type_psl = models.ForeignKey(Type_PSL, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0])
    # quantity = models.IntegerField()
    quantity_A_plus = models.IntegerField(default=0)
    quantity_A_m = models.IntegerField(default=0)
    quantity_B_plus = models.IntegerField(default=0)
    quantity_B_m = models.IntegerField(default=0)
    quantity_AB_plus = models.IntegerField(default=0)
    quantity_AB_m = models.IntegerField(default=0)
    quantity_O_plus = models.IntegerField(default=0)
    quantity_O_m = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def get_total_quantity(self):
        totat_quantity = self.quantity_A_m + self.quantity_A_plus + self.quantity_AB_m + self.quantity_AB_plus + self.quantity_B_m + self.quantity_B_plus + self.quantity_O_m + self.quantity_O_plus

        return totat_quantity
