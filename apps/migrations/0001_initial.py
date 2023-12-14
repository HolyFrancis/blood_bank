# Generated by Django 4.2.5 on 2023-12-14 11:28

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
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=255, unique=True)),
                ('volume', models.FloatField(choices=[(350, 350), (400, 400), (450, 450), (500, 500)], default=(450, 450))),
                ('sample', models.CharField(max_length=255, unique=True)),
                ('analysed', models.BooleanField(default=False)),
                ('state', models.CharField(choices=[('Eligible', 'Eligible'), ('Ineligible', 'Ineligible'), ('Attente', 'Analyse en Cours')], default=('Attente', 'Analyse en Cours'), max_length=255)),
                ('centrifuged', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('cni', models.CharField(max_length=255, unique=True)),
                ('birthday', models.DateField()),
                ('weight', models.IntegerField()),
                ('sex', models.CharField(choices=[('F', 'Féminin'), ('M', 'Masculin')], max_length=255)),
                ('blood_group', models.CharField(choices=[('O+', 'O+'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-')], max_length=255)),
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
                ('status', models.CharField(blank=True, choices=[('Eligible', 'Eligible'), ('En Attente', 'Attente'), ('Ineligible', 'Ineligible')], default=('En Attente', 'Attente'), max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type_psl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.product')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.stock')),
            ],
        ),
        migrations.CreateModel(
            name='PSL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=255, unique=True)),
                ('volume', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('blood', models.ManyToManyField(to='apps.blood')),
                ('type_psl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.type_psl')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.producttype'),
        ),
        migrations.AddField(
            model_name='product',
            name='psl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.psl'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.client')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Blood_analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.analysis')),
                ('blood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.blood')),
            ],
        ),
        migrations.AddField(
            model_name='blood',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.donor'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='product',
            field=models.ManyToManyField(to='apps.product'),
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
