from django.db import models
from roles.models import Roles

class Accounts(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	codename = models.CharField(max_length=100, unique=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	role = models.ForeignKey(
		Roles,
		on_delete=models.PROTECT
	)