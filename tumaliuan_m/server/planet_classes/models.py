from django.db import models


class PlanetClass(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200, unique=True)
	description = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)