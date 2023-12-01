from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
    path('pokemon_card_list', views.PokemonCardList.as_view(), name='pokemon-card-list'),
    path('collection_list', views.CollectionList.as_view(), name='collection-list'),
]
