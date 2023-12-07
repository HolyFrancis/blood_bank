# Generated by Django 4.2.5 on 2023-11-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_analysis_blood_client_donor_equipment_equipmenttype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='surgery',
            name='donor',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='had_surgery',
            new_name='anemia',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='has_disease',
            new_name='dentist',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='piercing',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='tattoo',
            new_name='examens',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='parteners',
        ),
        migrations.AddField(
            model_name='donor',
            name='infections',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donor',
            name='pregnancy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donor',
            name='status',
            field=models.CharField(blank=True, choices=[('Eligible', 'Eligible'), ('Attente', 'En Attente de Confirmation'), ('Ineligible', 'Ineligible')], default=('Attente', 'En Attente de Confirmation'), max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='surgery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donor',
            name='tattoo_piercing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donor',
            name='transfusion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donor',
            name='vaccine',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blood',
            name='state',
            field=models.CharField(choices=[('Eligible', 'Eligible'), ('Ineligible', 'Ineligible'), ('Attente', 'Analyse en Cours')], max_length=255),
        ),
        migrations.AlterField(
            model_name='donor',
            name='last_donation',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='donor',
            name='sex',
            field=models.CharField(choices=[('F', 'Féminin'), ('M', 'Masculin')], max_length=255),
        ),
        migrations.DeleteModel(
            name='Disease',
        ),
        migrations.DeleteModel(
            name='Medication',
        ),
        migrations.DeleteModel(
            name='Surgery',
        ),
    ]