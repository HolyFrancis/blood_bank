from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255, null = False, blank=False)
    phone = models.CharField(max_length=255, null = False, blank=False)
    email = models.CharField(max_length=255, null = False, blank=False)
    adress = models.CharField(max_length=255, null = False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name