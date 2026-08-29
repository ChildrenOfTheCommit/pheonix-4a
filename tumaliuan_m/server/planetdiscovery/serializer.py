from rest_framework import serializers

from planetdiscovery.models import PlanetDiscovery

class PlanetDiscoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetDiscovery
        fields = '__all__'
