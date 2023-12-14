from django.db import models

from apps.models.blood import Blood

class PSL(models.Model):
    TYPE_PSL = (
        ("GR","Globules Rouges"),
        ("PFC","Plasma Frais Congelé"),
        ("CPS","Concentré Plaquettaire Standard")
    )
    serial = models.CharField(max_length=255, null=False, blank=False, unique=True)
    volume = models.IntegerField(null=False, blank=False)
    type_psl = models.CharField(null=False, blank=False, choices=TYPE_PSL)
    blood = models.ManyToManyField(Blood)
    duration = models.IntegerField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    