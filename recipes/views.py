from django.shortcuts import render
from recipes.models import *
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm

# Create your views here.

def recipes_view(request):
    recipe_list = Recipe.objects.all()
    context={
        'recipe_list': recipe_list
    }
    return render(request, 'recipes/recipes.html', context=context)

def recipe_detail_view(request, slug=None):
    context = {}
    if slug is not None:
        recipe = Recipe.objects.get(slug=slug)
        context['recipe'] = recipe  
    return render(request, 'recipes/detail.html', context=context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        'form': form,
        'created': False,
    }
    if form.is_valid():
        recipe_object= form.save(commit=False)
        recipe_object.user = request.user
        recipe_object.save()
        context['created'] = True
        context['object'] = recipe_object
    
    return render(request, 'recipes/create.html', context=context)
    