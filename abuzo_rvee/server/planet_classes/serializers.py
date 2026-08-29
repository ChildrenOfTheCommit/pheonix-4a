from rest_framework import serializers
from .models import PlanetClasses

class PlanetClassesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanetClasses
        fields = '__all__'