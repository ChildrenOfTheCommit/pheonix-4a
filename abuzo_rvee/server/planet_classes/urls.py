from django.urls import path
from .views import PlanetClassesListCreate

urlpatterns = [
    path('planet_classes/', PlanetClassesListCreate.as_view()),
]