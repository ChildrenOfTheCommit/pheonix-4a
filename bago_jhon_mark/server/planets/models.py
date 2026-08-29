from django.db import models
from django.db.models import ForeignKey

from accounts.models import Accounts
from planet_classes.models import PlanetClass


class Planets(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200, unique=True)
	galaxy = models.CharField(max_length=200, null=True, blank=True)
	star_system = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	discover_date = models.DateField(max_length=200, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	owner = ForeignKey(
		Accounts,
		on_delete=models.SET_NULL,
		null=True,
		blank=True
	)

	planet_class = models.ForeignKey(
		PlanetClass,
		on_delete=models.SET_NULL,
		null=True,
		blank=True
	)