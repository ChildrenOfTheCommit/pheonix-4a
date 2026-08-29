from django.urls import path

from .views import PlanetClassListCreate, PlanetClassDetail

urlpatterns = [
	path('planet-class/', PlanetClassListCreate.as_view()),
	path('planet-class/<int:pk>/', PlanetClassDetail.as_view())
]