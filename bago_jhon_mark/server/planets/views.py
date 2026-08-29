from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Planets
from .serializers import PlanetSerializer


class PlanetsListCreate(APIView):
	def get(self, request):
		roles = Planets.objects.all()
		serializer = PlanetSerializer(roles, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = PlanetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(
			data=serializer.errors,
			status=status.HTTP_400_BAD_REQUEST
		)