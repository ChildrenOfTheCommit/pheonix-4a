# from django.urls import path
# from accounts.views import *
#
# urlpatterns = [
# 	path('login/', AccountLogin.as_view()),
#     path('register/', AccountRegister.as_view()),
# ]

from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', AccountLogin.as_view()),
    path('register/', AccountRegister.as_view()),

    path('accounts/', AccountList.as_view()),
    path('accounts/<int:pk>/', AccountDetail.as_view()),
    path('accounts/<int:pk>/update/', AccountUpdate.as_view()),
    path('accounts/<int:pk>/delete/', AccountDelete.as_view()),
]