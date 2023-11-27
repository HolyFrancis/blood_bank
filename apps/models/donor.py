from django.db import models

class Donor(models.Model):
    SEX = (("F", "Female"), ("M", "Male"))
    BLOOD_GROUP = (("O+", "O+"), ("A+", "A+"), ("B+", "B+"), ("AB+", "AB+"), ("O-", "O-"), ("A-", "A-"), ("B-", "B-"), ("AB-", "AB-"))
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=False, blank=False,max_length=255)
    cni = models.CharField(null=False, blank=False,max_length=255, unique=True)
    birthday = models.DateField(null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)
    sex = models.CharField(null=False, blank=False, max_length=255, choices=SEX)
    blood_group = models.CharField(null=False, blank=False, choices=BLOOD_GROUP, max_length=255)
    last_donation = models.DateField(null=False, blank=False)
    drugs = models.BooleanField(default=False)
    tattoo = models.BooleanField(default=False)
    piercing = models.BooleanField(default=False)
    parteners = models.IntegerField(null=False, blank=False, default=1)
    has_disease = models.BooleanField(default=False)
    had_surgery = models.BooleanField(default=False)
    under_medication = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    