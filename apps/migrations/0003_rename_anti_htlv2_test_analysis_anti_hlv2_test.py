# Generated by Django 4.2.5 on 2023-12-23 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_analysis_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysis',
            old_name='anti_htlv2_test',
            new_name='anti_hlv2_test',
        ),
    ]