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
		password = validated_data.pop('password') # sa model galing pero de makita dahil naka abstract user

		account = Accounts.objects.create(**validated_data) #** means include all values
		account.set_password(password)
		account.save()
		return account

	def update(self, instance, validated_data):
		password = (validated_data.pop('password', None))

		for attr, value in validated_data.items():
			setattr(instance, attr, value)

		if password:
			instance.set_password(password)
		instance.save()
		return instance

