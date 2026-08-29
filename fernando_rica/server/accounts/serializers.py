from rest_framework import serializers

from .models import Accounts


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
       model = Accounts
       fields = '__all__'
       extra_kwargs = {
          'password': {
             'write_only': True
          }
       }

    def create(self, validated_data):
       password = validated_data.pop('password')

       account = Accounts.objects.create(**validated_data)
       account.set_password(password)
       account.save()
       return account

    def update(self, instance, validated_data):
       password = validated_data.pop('password', None)

       for attr, value in validated_data.items():
          setattr(instance, attr, value)

       if password:
          instance.set_password(password)
       instance.save()
       return instance

