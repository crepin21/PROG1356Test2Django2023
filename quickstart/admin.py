from django.contrib import admin

# Register your models here.
# quickstart/admin.py

from django.contrib import admin
from .models import Capteur

admin.site.register(Capteur)
