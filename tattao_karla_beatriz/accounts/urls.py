from django.urls import path
from .views import *


urlpatterns = [
	path('login/', AccountLogin.as_view()),
	path('register/', AccountRegister.as_view()),

]