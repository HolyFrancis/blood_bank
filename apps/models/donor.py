from django.db import models
from django.utils.translation import gettext as _


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
        ("Attente", "En Attente"),
        ("Ineligible", "Ineligible"),
    )
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=50)
    cni = models.CharField(null=False, blank=False, max_length=50, unique=True)
    birthday = models.DateField(null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)
    sex = models.CharField(null=False, blank=False, max_length=50, choices=SEX)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=50)
    blood_group = models.CharField(null=True, blank=True, choices=BLOOD_GROUP, max_length=50)
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
    username = models.CharField(max_length=200, null=True, blank=True, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    class AppointmentStatus(models.TextChoices):
        ACCEPTED = "A", _("accepted")
        PENDING = "P", _("pending")
        REFUSED = "R", _("refused")

    donor = models.ForeignKey(
        "Donor",
        on_delete=models.DO_NOTHING,
        related_name="appointements",
        related_query_name="appointment",
    )
    created_at = models.DateTimeField(auto_now=True)
    date_to_be = models.DateTimeField(auto_now=False, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=1, choices=AppointmentStatus.choices, default=AppointmentStatus.PENDING)

    def __str__(self):
        return f"{self.donor.first_name} {self.donor.last_name}"
