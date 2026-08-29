from django.db import models
from planetclass.models import PlanetClass
from accounts.models import Account

class PlanetDiscovery(models.Model):
    id =  models.AutoField(primary_key=True)
    planetdiscovery = models.ForeignKey(PlanetClass, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    planet_name = models.CharField(max_length=100)
    galaxy =  models.CharField(max_length=100)
    star_system = models.CharField(max_length=100)
    description = models.TextField()
    discovery_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
