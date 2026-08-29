from django.urls import path
from .views import AccountLogin, AccountRegister

urlpatterns = [
	path('register/', AccountRegister.as_view()),
	path('login/', AccountLogin.as_view()),
]