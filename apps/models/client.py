from django.db import models

from apps.models import Users

class Client(models.Model):
    user = models.OneToOneField(Users, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null = False, blank=False)
    phone = models.CharField(max_length=50, null = False, blank=False)
    email = models.CharField(max_length=50, null = False, blank=False)
    adress = models.CharField(max_length=255, null = False, blank=False)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name