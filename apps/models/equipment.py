from django.db import models

from apps.models.type_psl import Type_psl
from apps.models.equipmentType import EquipmentType

class Equipment(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=False, blank=False)
    type_psl = models.ForeignKey(Type_psl, on_delete=models.CASCADE, null=True)
    equipmentType = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)