from typing import Any
from django.views.generic.list import ListView
from .models import PokemonCard, Trainer, Collection


# Create your views here.
class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 15    
    
    
class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon-card'
    template_name = 'pokemon-cards.html'
    paginate_by = 15    
    
    
class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collections.html'
    paginate_by = 15    
    