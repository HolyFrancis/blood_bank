# Generated by Django 4.2.5 on 2023-12-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_users_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Client', 'Client'), ('Docteur', 'Docteur'), ('Gestionnaire', 'Gestionnaire'), ('Laborantin', 'Laborantin'), ('Infirmier(e)', 'Infirmier(e)')], max_length=20, null=True),
        ),
    ]