from django.urls import path, include

urlpatterns = [
path('api/', include('roles.urls')),
path('api/', include('accounts.urls')),
path('api/', include('planetclass.urls')),
path('api/', include('planetdiscovery.urls')),
]
