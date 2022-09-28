from django.urls import path

from pokeapi.api.views import Pokemons


urlpatterns = [
    path('info/', Pokemons.as_view()),
]