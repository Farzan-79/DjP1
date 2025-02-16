from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import *
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeIngredientsForm, RecipeCreateNameForm
from django.forms.models import modelformset_factory
from django.http import HttpResponse, Http404 ,HttpResponseRedirect
from django.urls import reverse



def recipes_view(request):
    # recipe main page that will list out every existing recipe right now
    recipe_list = Recipe.objects.all()
    context={
        'recipe_list': recipe_list
    }
    return render(request, 'recipes/recipes.html', context=context)


def recipe_detail_view(request, slug=None):
    # detail of a recipe, this view is not doing anything special now, it just renders detail.html that has the headings
    # the hx_url is doing the main thing, it gets the url to the view below, which will load the real recipe detail while we are here 
    hx_url = reverse('recipes:hx-detail', kwargs={'slug':slug})
    context = {
        'hx_form_url' : hx_url
    }
    return render(request, 'recipes/detail.html', context=context)


def recipe_detail_hx_view(request, slug=None): 
    # this is so cool. it is powered by htmx. what i have done is: 1. the user gets to the detail url. 2- the url has a recipe header at top which loads instantly and also a loading under it that is actually just a text. 3- it tries to get data from THIS view, the hx-detail which the real content will be shown in its template, 4- so we are seeing the detail view, which has almost nothing in it but will load hx-detail view and show it to the user. 
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
    # first the name is submitted:
    form = RecipeCreateNameForm(request.POST or None)
    context = {
        'form' : form,
        'create': True,
    }
    if form.is_valid():
        #if it was a valid name,it will save it:
        new_recipe = form.save(commit=False)
        new_recipe.user = request.user
        new_recipe.save()

        update_context={
            'form_r' : RecipeForm(instance= new_recipe),
            'object' : new_recipe,
            'create' : True,
            'just_created': True,
            'create_ing_url' : reverse('recipes:hx-ing-create', kwargs={'parent_slug': new_recipe.slug})
        }
        # with the new context, and that we know the saved form was htmx, we can load the par-recipe-form with the newly created form as its instance so the user can add details and ings to it
        if request.htmx:
            return render(request, 'recipes/partials/par-recipe-form.html', context=update_context)
        # just to make sure... this shouldnt be redirected but if somehow there was a problem with htmx, here it is:
        return redirect(reverse('recipes:update', kwargs={'slug': new_recipe}))

    # if its being loaded for the first time, the create-update view will be rendered and from there htmx will take us to par-create-name
    # and if somehow the form was not valid, request.htmx is true, and we just will render the partial not the whole page
    if request.htmx:
        return render(request, 'recipes/partials/par-create-name.html', context=context)
    return render(request, 'recipes/create-update.html', context=context)

        
@login_required
def recipe_update_view(request, slug=None):
    obj = get_object_or_404(Recipe, slug=slug)
    # a form, with an instance found by the passed slug:
    form_r = RecipeForm(request.POST or None, instance=obj)
    # the url for creating a new ingredient form, wich will be connected to our instance at hand by the kwargs:
    create_ing_url = reverse('recipes:hx-ing-create', kwargs={'parent_slug': obj.slug})
    context = {
        'form_r': form_r,
        'object': obj,
        'update': True,
        'create_ing_url': create_ing_url,
    }
    if form_r.is_valid():
        form_r.save()
        context['message']= 'Data Saved Successfully'
        
    # the first time it will render create-update, when the form is submitted and request.htmx is true, it will only render the partial to avoid loading the whole page again. 
    if request.htmx:
        return render(request, 'recipes/partials/par-recipe-form.html', context=context)
    return render(request, 'recipes/create-update.html', context=context)


def ingredient_update_view(request, parent_slug=None, id=None):
    # this view is for editing or creating the ingredients that already exist in the recipe we have
    # we can find out edit or create by looking at the id, if the ing has an id, we should update it if not its being created
    if not request.htmx:
        return Http404
    
    # it MUST have a parent recipe
    try:
        parent_recipe = Recipe.objects.get(slug=parent_slug, user=request.user)
    except:
        parent_recipe = None
    if parent_recipe == None:
        return HttpResponse('not found')
    
    # instance being none means it didnt exist before and we should give the user a new ing form to create it, if its not none then it existed and we should give a form that contains it for the user to edit it
    instance = None
    if id is not None:
        try:
            instance = RecipeIngredients.objects.get(id=id, recipe=parent_recipe)
        except:
            instance = None
    
    # this is the url, if there is an instance, it will be edit and else it will be create url
    # its used to determine the url the hx-post on par-ingredient-form will post the data, both will come back here but with the right url so it can know which it is
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
        # the newly created or edited ing will be sent to par-ingredient to be shown to the user 
        return render(request, 'recipes/partials/par-ingredients.html', context=context)
    
    # this is the edit/create form that needed the url, it will get the instance if it exists, or create a new form if it doesnt.
    # when saved, it will be shown in par-ingredients as a new data
    return render(request, 'recipes/partials/par-ingredient-form.html', context=context)
    
    