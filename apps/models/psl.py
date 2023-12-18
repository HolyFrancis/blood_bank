from django.db import models

from apps.models.blood import Blood
from apps.models.solution import Solution


class Price(models.Model):
    TYPE = (("GR","Globules Rouges"),("PFC","Plasma Frais Congelé"),("CPS","Concentré Plaquettaire Standard"))
    typ = models.CharField(max_length=50, choices=TYPE, null=False, blank=False, unique=True)
    price = models.IntegerField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.price)
    
    
class PSL(models.Model):
    TYPE = (("GR","Globules Rouges"),("PFC","Plasma Frais Congelé"),("CPS","Concentré Plaquettaire Standard"))
    serial = models.CharField(max_length=50, null=False, blank=False, unique=True)
    typ = models.ForeignKey(max_length=50, choices=TYPE, null=False, blank=False)
    volume = models.IntegerField(null=False, blank=False)
    blood = models.ManyToManyField(Blood)
    duration = models.IntegerField(null=True, blank=True)
    price = models.ForeignKey(Price, null=True, blank=True, on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
