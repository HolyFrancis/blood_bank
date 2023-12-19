# Generated by Django 4.2.5 on 2023-12-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(blank=True, choices=[('Eligible', 'Eligible'), ('Attente', 'En Attente'), ('Ineligible', 'Ineligible')], default=('Attente', 'En Attente'), max_length=50, null=True),
        ),
    ]