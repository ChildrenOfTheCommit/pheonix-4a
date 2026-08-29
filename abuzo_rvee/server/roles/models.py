from django.db import models


class Roles(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)