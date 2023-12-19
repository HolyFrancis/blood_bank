from django.db import models

class Type_PSL(models.Model):
    TYPE = (("GR","Globules Rouges"),("PFC","Plasma Frais Congelé"),("CPS","Concentré Plaquettaire Standard"))
    name = models.CharField(max_length=50,blank=False,null=False, choices=TYPE, unique=True)
    price = models.IntegerField(blank=False,null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name