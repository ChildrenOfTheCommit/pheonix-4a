from rest_framework import serializers

from .models import Planets


class PlanetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Planets
		fields = '__all__'