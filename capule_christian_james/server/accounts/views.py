from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import Accounts
from accounts.serializers import AccountSerializer


class AccountLogin(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')

		if not username or not password:
			return Response (
			data = {
				'message': 'Username and password are required'
			},

			status = status.HTTP_400_BAD_REQUEST)
		
		account = authenticate(username=username, password=password)

		if account is None:
			return Response(
				data={'message': 'Username or password is invalid'},
				status=status.HTTP_401_UNAUTHORIZED
			)

		refresh = RefreshToken.for_user(account)
		serializer = AccountSerializer(account)
		return Response (
			data = {
				'message': 'Login Successful',
				'account': serializer.data,
				'tokens': {
					'refresh': str(refresh),
					'access': str(refresh.access_token)
				}
			},

			status = status.HTTP_200_OK

		)

class AccountRegister(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		serializer = AccountSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(
				data = serializer.data, status=HTTP_201_CREATED
			)

		return Response(
			data = serializer.errors, status = status.HTTP_400_BAD_REQUEST
		)

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