from django.db import models

# Create your models here.
class Roaster(models.Model):
    name = models.CharField(max_length=256)
    location_friendly = models.CharField(max_length=256)

class Store(models.Model):
    name = models.CharField(max_length=256)
    url =  models.URLField()
    location_friendly = models.CharField(max_length=256)

class Coffee(models.Model):
    name = models.CharField(max_length=256)
    roaster = models.ForeignKey(Roaster, on_delete=models.SET_NULL, null=True)
    stores = models.ManyToManyField(Store)
