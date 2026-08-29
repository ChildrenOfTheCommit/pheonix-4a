from django.urls import path
from roles.views import RoleListCreate

urlpatterns = [
    path('roles/', RoleListCreate.as_view())
]