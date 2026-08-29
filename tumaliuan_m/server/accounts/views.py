from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from accounts.models import Account
from accounts.serializer import AccountSerializer

class AccountListView(APIView):
    def get(self, request):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDeleteListView(APIView):
        def delete(self, request, pk):
            try:
                account = Account.objects.get(pk=pk)
            except Account.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
