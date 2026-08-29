from django.urls import path
from .views import PlanetListCreate

urlpatterns = [
    path('planet/', PlanetListCreate.as_view())
]