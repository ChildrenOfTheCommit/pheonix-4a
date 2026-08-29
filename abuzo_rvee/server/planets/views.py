from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from planets.models import Planets
from planets.serializers import PlanetsSerializer

class PlanetsListCreate(APIView):
    def get(self,request):
        planets = Planets.objects.all()
        serializer = PlanetsSerializer(planets, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PlanetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {'message': 'Invalid :P'},
            status = status.HTTP_400_BAD_REQUEST
        )