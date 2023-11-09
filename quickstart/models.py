from django.db import models
from django.contrib import admin

# Create your models here.
class Capteur(models.Model):
    nomUc       = models.fields.CharField(max_length=8)
    nomCapteur  = models.fields.CharField(max_length=8)
    temperature = models.fields.CharField(max_length=8)
  #  humidite    = models.fields.CharField(max_length=8)
