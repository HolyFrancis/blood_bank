from django.db import models

class Reactant(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    description = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name