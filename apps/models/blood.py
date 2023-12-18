from django.db import models

from apps.models.donor import Donor


class Blood(models.Model):
    STATE = (
        ("Eligible", "Eligible"),
        ("Ineligible", "Ineligible"),
        ("Attente", "Analyse en Cours"),
    )
    VOLUME = ((350, 350), (400, 400), (450, 450), (500, 500))
    serial = models.CharField(max_length=50, blank=False, null=False, unique=True)
    volume = models.FloatField(null=False, blank=False, choices=VOLUME, default=VOLUME[2])
    sample = models.CharField(max_length=50, null=False, blank=False, unique=True)
    analysed = models.BooleanField(default=False)
    state = models.CharField(max_length=50, choices=STATE, default=STATE[2])
    centrifuged = models.BooleanField(default=False)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Poche N°{self.serial} de {self.volume} ml"
