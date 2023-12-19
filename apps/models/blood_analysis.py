from django.db import models

from apps.models.blood import Blood
from apps.models.analysis import Analysis

class Blood_analysis(models.Model):
    RESULT = (("Sain","Sain"), ("Contaminé","Contaminé"))
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    result = models.CharField(max_length=50, null=False, blank=False, choices=RESULT)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)