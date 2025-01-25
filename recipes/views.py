from django.shortcuts import render, get_object_or_404, redirect
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
        try:
            #recipe = Recipe.objects.get(slug=slug)
            recipe = get_object_or_404(Recipe, slug=slug)  
        except Recipe.MultipleObjectsReturned:
            recipe = Recipe.objects.filter(slug=slug).first()
        context['recipe'] = recipe

    return render(request, 'recipes/detail.html', context=context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        'form': form,
        'create': True,
    }
    if form.is_valid():
        recipe_object= form.save(commit=False)
        recipe_object.user = request.user
        recipe_object.save()
        context['message'] = 'Your Recipe has been created successfully'
        context['object'] = recipe_object
    
    return render(request, 'recipes/create.html', context=context)

@login_required
def recipe_update_view(request, slug=None):
    obj = get_object_or_404(Recipe, slug=slug, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'object': obj,
        'update': True
    }
    if form.is_valid():
        form.save()
        context['message']= 'Recipe Updated Successfully'
        #return redirect(obj.get_absolute_urls())
    return render(request, 'recipes/create.html', context=context)
    