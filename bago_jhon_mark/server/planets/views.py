from rest_framework.response import Response
from rest_framework.views import APIView
from planets.models import Planet
from planets.serializers import PlanetSerializer
from rest_framework import status



class PlanetListCreate(APIView):
    def get(self, request):
        planets = Planet.objects.all()
        serializer = PlanetSerializer(planets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {'message':'Invalid :P'},
            status=status.HTTP_400_BAD_REQUEST
        )

#http://localhost:8000/api/roles/