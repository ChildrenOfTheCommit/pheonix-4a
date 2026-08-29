from django.db import models


from planet_classes.models import PlanetClass
from accounts.models import Accounts

class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    Planet = models.CharField()
    Galaxy = models.CharField()
    Star_System = models.CharField()
    Discovery_Date = models.DateTimeField()

    Owner = models.ForeignKey(
        Accounts,
        on_delete=models.PROTECT,
    )

    Class = models.ForeignKey(
    PlanetClass,
    on_delete=models.PROTECT
    )


    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
