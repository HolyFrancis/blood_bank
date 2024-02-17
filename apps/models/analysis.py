from django.db import models

from apps.models.blood import Blood


class Analysis(models.Model):
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
    RESULT = (("Positif", "Positif"), ("Négatif", "Négatif"))
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    irregular_antibodies = models.CharField(max_length=50, null=False, blank=False, choices=RESULT)
    hiv_test = models.CharField(max_length=50, null=False, blank=False, choices=RESULT)
    hepatites_test = models.CharField(max_length=50, null=False, blank=False, choices=RESULT)
    anti_hlv1_test = models.CharField(max_length=50, null=False, blank=False, choices=RESULT)
    anti_hlv2_test = models.CharField(max_length=50, null=False, blank=False, choices=RESULT)
    malaria_test = models.CharField(max_length=50, null=False, blank=False, choices=RESULT)
    blood_group = models.CharField(max_length=50, null=True, blank=True, choices=BLOOD_GROUP)
    result = models.CharField(max_length=50, null=False, blank=False, choices=RESULT, default=RESULT[0])
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.blood.serial
