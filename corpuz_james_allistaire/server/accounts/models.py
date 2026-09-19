from django.contrib.auth.models import AbstractUser
from django.db import models
from roles.models import Roles

class Accounts(AbstractUser):
	codename = models.CharField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	role = models.ForeignKey(
		Roles,
		on_delete=models.PROTECT
	)