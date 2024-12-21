from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Trainer

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer. objects.all ()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons,
        'triaers' : trainers 
        }, 
        request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_detail(request, trainer_id):
    trainer = Trainer.objects.get(pk = trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'traier': trainer
    }
    return HttpResponse(template.render(context, request))