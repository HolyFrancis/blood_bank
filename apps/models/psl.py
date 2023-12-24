from django.db import models

from apps.models.blood import Blood
from apps.models.type_psl import Type_PSL
from apps.models.solution import Solution
from apps.models.order import Order


class PSL(models.Model):
    serial = models.CharField(max_length=50, null=False, blank=False, unique=True)
    type_psl = models.ForeignKey(Type_PSL, on_delete=models.CASCADE)
    volume = models.IntegerField(null=False, blank=False)
    dispo = models.BooleanField(default=True)
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True, blank=True)
    solution = models.ForeignKey(Solution, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
