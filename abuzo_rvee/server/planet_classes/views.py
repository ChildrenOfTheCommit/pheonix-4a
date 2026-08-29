from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PlanetClass
from .serializers import PlanetClassSerializer


class PlanetClassListCreate(APIView):
	def get(self, request):
		planet_classes = PlanetClass.objects.all()
		serializer = PlanetClassSerializer(planet_classes, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = PlanetClassSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(
			data=serializer.errors,
			status=status.HTTP_400_BAD_REQUEST
		)


class PlanetClassDetail(APIView):
	def get(self, request, pk):
		planet_class = get_object_or_404(PlanetClass, pk=pk)
		serializer = PlanetClassSerializer(planet_class)
		return Response(serializer.data)

	def put(self, request, pk):
		try:
			planet_class = PlanetClass.objects.get(pk=pk)
		except PlanetClass.DoesNotExist:
			return Response(
				data={'message': 'Planet Class does not exist'},
				status=status.HTTP_404_NOT_FOUND
			)
		serializer = PlanetClassSerializer(planet_class, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(
			data=serializer.errors,
			status=status.HTTP_400_BAD_REQUEST
		)

	def delete(self, request, pk):
		try:
			planet_class = PlanetClass.objects.get(pk=pk)
		except PlanetClass.DoesNotExist:
			return Response(
				data={'message': 'Planet Class does not exist'},
				status=status.HTTP_404_NOT_FOUND
			)
		planet_class.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)