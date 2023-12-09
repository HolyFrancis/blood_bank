from django.db import models


class Type_psl(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    duration = models.DateTimeField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
