from django.db import models

from apps.models.donor import Donor

class Blood(models.Model):
    STATE = (("Eligible","Eligible"), ("Ineligible","Ineligible"), ("Pending Analyse","Pending Analyse"))
    VOLUME = (("350","350"), ("400","400"),("450","450"),("500","500"))
    serial = models.CharField(max_length=255, blank=False, null=False)
    volume = models.FloatField(null=False, blank=False, choices=VOLUME)
    sample = models.CharField(max_length=255,null=False, blank=False)
    analysed = models.BooleanField(default=False)
    state = models.CharField(max_length=255,choices=STATE)
    centrifuged = models.BooleanField(default=False)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)