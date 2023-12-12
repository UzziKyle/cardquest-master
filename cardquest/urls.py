from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('pokemon_card_list/add', views.PokemonCardCreateView.as_view(), name='pokemon-card-add'),
    path('pokemon_card_list/<pk>', views.PokemonCardUpdateView.as_view(), name='pokemon-card-update'),
    path('pokemon_card_list/<pk>/delete', views.PokemonCardDeleteView.as_view(), name='pokemon-card-delete'),
    path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', views.TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', views.TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', views.TrainerDeleteView.as_view(), name='trainer-delete'),
    path('pokemon_card', views.PokemonCardList.as_view(), name='pokemon-card'),
    path('collection_list', views.CollectionList.as_view(), name='collection-list'),
]
