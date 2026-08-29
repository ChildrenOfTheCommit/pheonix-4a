from django.urls import path
from roles.views import RoleListView, RoleDeleteListView

urlpatterns = [
    path('roles/', RoleListView.as_view()),
    path('roles/<int:pk>/', RoleDeleteListView.as_view()),
]
