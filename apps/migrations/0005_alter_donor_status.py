# Generated by Django 4.2.5 on 2023-12-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_donor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(blank=True, choices=[('Eligible', 'Eligible'), ('En Attente', 'Attente'), ('Ineligible', 'Ineligible')], default=('En Attente', 'Attente'), max_length=255, null=True),
        ),
    ]
