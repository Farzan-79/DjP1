from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import *
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeIngredientsForm
from django.forms.models import modelformset_factory
from django.http import HttpResponse, Http404
from django.urls import reverse

# Create your views here.

def recipes_view(request):
    recipe_list = Recipe.objects.all()
    context={
        'recipe_list': recipe_list
    }
    return render(request, 'recipes/recipes.html', context=context)

def recipe_detail_view(request, slug=None):
    hx_url = reverse('recipes:hx-detail', kwargs={'slug':slug})
    context = {
        'hx_form_url' : hx_url
    }

    return render(request, 'recipes/detail.html', context=context)

def recipe_detail_hx_view(request, slug=None): 
    # this is so cool. it is powered by htmx. what i have done is: 1. the user gets to the detail url. 2- the url has a recipe name at top which loads instantly and also a loading under it that is actually just a text. 3- it tries to get data from THIS view, the hx-detail which the real content will be shown in its template, 4- so we are seeing the detail view, which has almost nothing in it but will load hx-detail view and show it to the user. 
    if not request.htmx:
        return Http404
    context = {}
    if slug is not None:
        try:
            recipe = Recipe.objects.get(slug=slug)  
        except:
            recipe = None
        if recipe is None:
            return HttpResponse('not found')
        context['recipe'] = recipe

    return render(request, 'recipes/partials/par-detail.html', context=context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    create_ing_url = reverse('recipes:hx-ing-create', kwargs={'parent_slug': obj.slug})
    context = {
        'form_r': form,
        'create': True,
        'create_ing_url': create_ing_url,
    }
    if form.is_valid():
        recipe_object= form.save(commit=False)
        recipe_object.user = request.user
        recipe_object.save()
        context['message'] = 'Your Recipe has been created successfully'
        context['object'] = recipe_object
    if request.htmx:
        return render(request, 'recipes/partials/par-recipe-form.html', context=context) 
    return render(request, 'recipes/create-update.html', context=context)

@login_required
def recipe_update_view(request, slug=None):
    obj = get_object_or_404(Recipe, slug=slug)
    form_r = RecipeForm(request.POST or None, instance=obj)
    create_ing_url = reverse('recipes:hx-ing-create', kwargs={'parent_slug': obj.slug})
    #RecipeIngredientsFormSet = modelformset_factory(RecipeIngredients, RecipeIngredientsForm, extra=0)
    #form_i = RecipeIngredientsFormSet(request.POST or None, queryset = obj.ings.all())
    context = {
        'form_r': form_r,
        #'form_i': form_i,
        'object': obj,
        'update': True,
        'create_ing_url': create_ing_url,
    }
    if form_r.is_valid():
        form_r.save()
        context['message']= 'Recipe Updated Successfully'
    #if all([form_r.is_valid(), form_i.is_valid()]):
    #    parent = form_r.save(commit=False)
    #    parent.save()
    #    for item in form_i:
    #        child = item.save(commit=False)
    #        child.recipe = parent
    #        child.save()

        
    
    if request.htmx:
        return render(request, 'recipes/partials/par-recipe-form.html', context=context)
    return render(request, 'recipes/create-update.html', context=context)


def ingredient_update_view(request, parent_slug=None, id=None):
    if not request.htmx:
        return Http404
    
    try:
        parent_recipe = Recipe.objects.get(slug=parent_slug, user=request.user)
    except:
        parent_recipe = None
    if parent_recipe == None:
        return HttpResponse('not found')
    
    instance = None
    if id is not None:
        try:
            instance = RecipeIngredients.objects.get(id=id, recipe=parent_recipe)
        except:
            instance = None
    
    url = instance.get_hx_update_url() if instance else reverse('recipes:hx-ing-create', kwargs={'parent_slug':parent_recipe.slug})

    form = RecipeIngredientsForm(request.POST or None, instance= instance)
    context = {
        'object' : instance,
        'form' : form,
        'url': url,
    }

    if form.is_valid():
        new_ing = form.save(commit=False)
        if instance is None:
            new_ing.recipe = parent_recipe
        new_ing.save()
        context['object'] = new_ing
        return render(request, 'recipes/partials/par-ingredients.html', context=context)
    
    return render(request, 'recipes/partials/par-ingredient-form.html', context=context)
    
    