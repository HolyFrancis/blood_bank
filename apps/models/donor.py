from django.db import models


class Donor(models.Model):
    SEX = (("F", "Féminin"), ("M", "Masculin"))
    BLOOD_GROUP = (
        ("O+", "O+"),
        ("A+", "A+"),
        ("B+", "B+"),
        ("AB+", "AB+"),
        ("O-", "O-"),
        ("A-", "A-"),
        ("B-", "B-"),
        ("AB-", "AB-"),
    )
    STATUS = (
        ("Eligible", "Eligible"),
        ("En Attente", "Attente"),
        ("Ineligible", "Ineligible"),
    )
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    cni = models.CharField(null=False, blank=False, max_length=50, unique=True)
    birthday = models.DateField(null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)
    sex = models.CharField(null=False, blank=False, max_length=50, choices=SEX)
    blood_group = models.CharField(null=False, blank=False, choices=BLOOD_GROUP, max_length=50)
    last_donation = models.BooleanField(null=False, blank=False)
    drugs = models.BooleanField(default=False)
    tattoo_piercing = models.BooleanField(default=False)
    disease = models.BooleanField(default=False)
    surgery = models.BooleanField(default=False)
    under_medication = models.BooleanField(default=False)
    vaccine = models.BooleanField(default=False)
    dentist = models.BooleanField(default=False)
    pregnancy = models.BooleanField(default=False)
    transfusion = models.BooleanField(default=False)
    anemia = models.BooleanField(default=False)
    infections = models.BooleanField(default=False)
    examens = models.BooleanField(default=False)
    status = models.CharField(null=True, blank=True, choices=STATUS, default=STATUS[1], max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
