from django.urls import path

from planetclass.views import PlanetClassList,PlanetClassDeleteList

urlpatterns = [
    path('planetclass/', PlanetClassList.as_view()),
    path('planetclass/<int:pk>/', PlanetClassDeleteList.as_view()),
]