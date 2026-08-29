from django.urls import path
from .views import PlanetClassListCreate

urlpatterns = [
    path('planetclass/', PlanetClassListCreate.as_view())
]