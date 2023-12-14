from django.db import models

from apps.models.blood import Blood
from apps.models.type_psl import Type_psl

class PSL(models.Model):
    serial = models.CharField(max_length=255, null=False, blank=False, unique=True)
    volume = models.IntegerField(null=False, blank=False)
    type_psl = models.ForeignKey(Type_psl, on_delete=models.CASCADE)
    blood = models.ManyToManyField(Blood)
    duration = models.IntegerField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    