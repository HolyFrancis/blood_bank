# Generated by Django 4.2.5 on 2023-12-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_delete_reactant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
