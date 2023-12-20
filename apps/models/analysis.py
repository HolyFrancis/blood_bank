from django.db import models

from apps.models.reactant import Reactant
from apps.models.blood import Blood

class Analysis(models.Model):
    RESULT = (("Positif","Positif"), ("Négatif","Négatif"))
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    result = models.CharField(max_length=50, null=False, blank=False, choices=RESULT)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.typ