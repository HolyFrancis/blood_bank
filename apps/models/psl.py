from django.db import models
from datetime import datetime

from apps.models.type_psl import Type_psl
from apps.models.blood import Blood

class PSL(models.Model):
    serial = models.CharField(max_length=255, null=False, blank=False)
    volume = models.IntegerField(null=False, blank=False)
    start_date = models.DateTimeField(null=False,blank=False, default=datetime.now)
    end_date = models.DateTimeField(null=False,blank=False)
    type_psl = models.ForeignKey(Type_psl, on_delete=models.CASCADE)
    blood = models.ManyToManyField(Blood)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    