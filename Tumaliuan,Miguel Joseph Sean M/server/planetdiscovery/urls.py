from django.urls import path

from planetdiscovery.views import PlanetDiscoveryListView, PlanetDiscoveryDeleteListView

urlpatterns = [
path('planetdiscovery/', PlanetDiscoveryListView.as_view()),
path('planetdiscovery/<int:pk>/', PlanetDiscoveryDeleteListView.as_view()),
]