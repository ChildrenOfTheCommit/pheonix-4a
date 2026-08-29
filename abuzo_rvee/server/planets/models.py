from django.db import models

class Planets(models.Model):
    id = models.AutoField(primary_key=True)
    planet_class_id = models.IntegerField()
    planet = models.CharField(max_length=200)
    galaxy = models.CharField(max_length=200)
    star_system = models.CharField(max_length=200)
    discovery_date = models.DateField()
    owner = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
