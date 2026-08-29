from rest_framework.response import Response
from rest_framework.views import APIView
from planet_classes.models import PlanetClass
from planet_classes.serializers import PlanetClassSerializer
from rest_framework import status



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
            {'message':'Invalid :P'},
            status=status.HTTP_400_BAD_REQUEST
        )

#http://localhost:8000/api/roles/