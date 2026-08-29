from django.urls import path, include

urlpatterns = [
	path('api/', include('roles.urls')),
	path('api/', include('accounts.urls')),
	path('api/', include('planet_classes.urls')),
	path('api/', include('planets.urls'))
]