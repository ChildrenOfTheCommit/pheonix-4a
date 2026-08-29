from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Accounts
from accounts.serializers import AccountSerializer


class AccountListCreate(APIView):
	def get(self, request):
		accounts = Accounts.objects.all()
		serializer = AccountSerializer(accounts, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = AccountSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(
			data=serializer.errors,
			status=status.HTTP_400_BAD_REQUEST
		)