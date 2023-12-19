from django.db import models

from apps.models.reactant import Reactant

class Analysis(models.Model):
    typ = models.CharField(max_length=50, null=False, blank=False)
    reactant = models.ManyToManyField(Reactant)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.typ