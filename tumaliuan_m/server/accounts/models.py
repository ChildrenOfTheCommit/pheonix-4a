from django.db import models
from roles.models import Role

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    codename = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


