from django.urls import path
from .views import AccountListCreate

urlpatterns = [
    path('accounts/', AccountListCreate.as_view()),
]