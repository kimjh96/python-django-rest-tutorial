from django.urls import path
from .views import board_list

urlpatterns = [
    path('boards', board_list, name='board_list'),
]