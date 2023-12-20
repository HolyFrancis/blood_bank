# Generated by Django 4.2.5 on 2023-12-20 15:38

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=50, unique=True)),
                ('volume', models.FloatField(choices=[(350, 350), (400, 400), (450, 450), (500, 500)], default=(450, 450))),
                ('sample', models.CharField(max_length=50, unique=True)),
                ('analysed', models.BooleanField(default=False)),
                ('state', models.CharField(choices=[('Eligible', 'Eligible'), ('Ineligible', 'Ineligible'), ('Attente', 'Analyse en Cours')], default=('Attente', 'Analyse en Cours'), max_length=50)),
                ('centrifuged', models.BooleanField(default=False)),
                ('gr', models.BooleanField(default=False)),
                ('pfc', models.BooleanField(default=False)),
                ('cps', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cni', models.CharField(max_length=50, unique=True)),
                ('birthday', models.DateField()),
                ('weight', models.IntegerField()),
                ('sex', models.CharField(choices=[('F', 'Féminin'), ('M', 'Masculin')], max_length=50)),
                ('blood_group', models.CharField(choices=[('O+', 'O+'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-')], max_length=50)),
                ('last_donation', models.BooleanField()),
                ('drugs', models.BooleanField(default=False)),
                ('tattoo_piercing', models.BooleanField(default=False)),
                ('disease', models.BooleanField(default=False)),
                ('surgery', models.BooleanField(default=False)),
                ('under_medication', models.BooleanField(default=False)),
                ('vaccine', models.BooleanField(default=False)),
                ('dentist', models.BooleanField(default=False)),
                ('pregnancy', models.BooleanField(default=False)),
                ('transfusion', models.BooleanField(default=False)),
                ('anemia', models.BooleanField(default=False)),
                ('infections', models.BooleanField(default=False)),
                ('examens', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, choices=[('Eligible', 'Eligible'), ('Attente', 'En Attente'), ('Ineligible', 'Ineligible')], default=('Attente', 'En Attente'), max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reactant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type_PSL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('GR', 'Globules Rouges'), ('PFC', 'Plasma Frais Congelé'), ('CPS', 'Concentré Plaquettaire Standard')], max_length=50, unique=True)),
                ('price', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PSL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=50, unique=True)),
                ('volume', models.IntegerField()),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('blood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.blood')),
                ('solution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.solution')),
                ('type_psl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.type_psl')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('En Attente', 'En Attente'), ('Délivrée', 'Délivrée'), ('Annulée', 'Annulée')], default=('En Attente', 'En Attente'), max_length=50)),
                ('quantity', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.client')),
                ('type_psl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.type_psl')),
            ],
        ),
        migrations.AddField(
            model_name='blood',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.donor'),
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('Positif', 'Positif'), ('Négatif', 'Négatif')], max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('blood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.blood')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
