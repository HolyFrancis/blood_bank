from django.contrib import admin

from apps.models import Users
from apps.models import Client
from apps.models import Order,Location

admin.site.register(Users)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Location)

