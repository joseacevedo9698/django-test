from django.urls import path
from . import views

urlpatterns = [
    path('', views.summoner_list, name='summoner_list'),
]