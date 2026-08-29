from rest_framework import serializers

from .models import PlanetClass


class PlanetClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetClass
        fields = '__all__'
