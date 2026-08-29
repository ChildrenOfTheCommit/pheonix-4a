from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from planetdiscovery.models import PlanetDiscovery
from planetdiscovery.serializer import PlanetDiscoverySerializer

class PlanetDiscoveryListView(APIView):
    def get(self, request):
            planet_discovery =PlanetDiscovery.objects.all()
            serializer = PlanetDiscoverySerializer(planet_discovery, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PlanetDiscoverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlanetDiscoveryDeleteListView(APIView):
    def delete(self, request, pk):
        try:
            account = PlanetDiscovery.objects.get(pk=pk)
        except PlanetDiscovery.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
