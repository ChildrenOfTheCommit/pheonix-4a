from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from planetclass.models import PlanetClass
from planetclass.serializer import PlanetClassSerializer

class PlanetClassList(APIView):
    def get(self, request, format=None):
        planet_class_list = PlanetClass.objects.all()
        serializer = PlanetClassSerializer(planet_class_list, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PlanetClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlanetClassDeleteList(APIView):
    def delete(self, request,pk,format=None):
        try:
            planet_class = PlanetClass.objects.get(pk=pk)
        except PlanetClass.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        planet_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
