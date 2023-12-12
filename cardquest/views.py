from typing import Any
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import PokemonCard, Trainer, Collection
from .forms import TrainerForm, PokemonCardForm
from django.urls import reverse_lazy


# Create your views here.
class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
   

class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_card_add.html'
    success_url = reverse_lazy('home')
    

class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_card_edit.html'
    success_url = reverse_lazy('home')
    

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_card_del.html'
    success_url = reverse_lazy('home')
    
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainer.html'
    paginate_by = 15   
    
    
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')
    
    
class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')
        
    
class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list') 
    
    
class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon-card'
    template_name = 'pokemon_card.html'
    paginate_by = 15    

    
class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collections.html'
    paginate_by = 15    
    
