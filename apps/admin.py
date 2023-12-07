from django.contrib import admin

from apps.models import Users
from .models import Client

admin.site.register(Users)
admin.site.register(Client)

