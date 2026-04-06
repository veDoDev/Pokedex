from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.home, name='home'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='pokemon_detail'),
]