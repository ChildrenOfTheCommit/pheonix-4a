from django.urls import path

from .views import PlanetsListCreate

urlpatterns = [
	path('planets/', PlanetsListCreate.as_view())
]