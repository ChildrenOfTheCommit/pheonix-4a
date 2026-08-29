from rest_framework import serializers
from accounts.models import Accounts

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'