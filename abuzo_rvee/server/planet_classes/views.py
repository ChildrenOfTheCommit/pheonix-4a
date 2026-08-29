from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from planet_classes.models import PlanetClasses
from planet_classes.serializers import PlanetClassesSerializer

class PlanetClassesListCreate(APIView):
    def get(self,request):
        planetclasses = PlanetClasses.objects.all()
        serializer = PlanetClassesSerializer(planetclasses, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PlanetClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {'message': 'Invalid :P'},
            status = status.HTTP_400_BAD_REQUEST
        )