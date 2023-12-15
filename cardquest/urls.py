from django.urls import path
from . import views


urlpatterns = [
    # Home
    path('', views.HomePageView.as_view(), name='home'),
    
    # Trainers
    path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', views.TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', views.TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', views.TrainerDeleteView.as_view(), name='trainer-delete'),
    
    # Pokemons
    path('pokemoncard_list', views.PokemonCardList.as_view(), name='pokemoncard-list'),
    path('pokemoncard_list/add', views.PokemonCardCreateView.as_view(), name='pokemoncard-add'),
    path('pokemoncard_list/<pk>', views.PokemonCardUpdateView.as_view(), name='pokemoncard-update'),
    path('pokemoncard_list/<pk>/delete', views.PokemonCardDeleteView.as_view(), name='pokemoncard-delete'),
    
    # Collections
    path('collection_list', views.CollectionList.as_view(), name='collection-list'),
    path('collection_list/add', views.CollectionCreateView.as_view(), name='collection-list-add'),
    path('collection_list/<pk>', views.CollectionUpdateView.as_view(), name='collection-list-update'),
    path('collection_list/<pk>/delete', views.CollectionDeleteView.as_view(), name='collection-list-delete'),
]
