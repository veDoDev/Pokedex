from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Pokemon

def home(request):
    # Get search query if any
    search_query = request.GET.get('search', '')
    
    # Get sort parameter
    sort_by = request.GET.get('sort', 'id')
    
    # Filter Pokémon based on search query
    if search_query:
        # Try to parse as integer for ID search
        try:
            pokemon_id = int(search_query)
            pokemon_list = Pokemon.objects.filter(id=pokemon_id)
        except ValueError:
            # If not an integer, search by name
            pokemon_list = Pokemon.objects.filter(name__icontains=search_query)
    else:
        pokemon_list = Pokemon.objects.all()
    
    # Apply sorting
    pokemon_list = pokemon_list.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(pokemon_list, 12)  # Show 12 Pokémon per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    
    return render(request, 'Pokedex/home.html', context)

def pokemon_detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    
    # Get previous and next Pokémon
    prev_pokemon = Pokemon.objects.filter(id__lt=pokemon_id).order_by('-id').first()
    next_pokemon = Pokemon.objects.filter(id__gt=pokemon_id).order_by('id').first()
    
    context = {
        'pokemon': pokemon,
        'prev_pokemon': prev_pokemon,
        'next_pokemon': next_pokemon,
    }
    
    return render(request, 'Pokedex/detail.html', context)
