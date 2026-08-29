from django.urls import path
from accounts.views import AccountListView, AccountDeleteListView

urlpatterns = [
    path('accounts/', AccountListView.as_view()),
    path('accounts/<int:pk>/', AccountDeleteListView.as_view()),
]