from django.shortcuts import render
from recipes.models import Recipe
from articles.models import Article

# Create your views here.

def search_view(request):
    query = request.GET.get('q')
    found_recipes= Recipe.objects.search(query)
    found_articles = Article.objects.search(query)
    if not found_recipes.exists() and not found_articles.exists():
        no_result = True
    else:
        no_result = False

    context= {
        'articles': found_articles,
        'recipes': found_recipes,
        'no_result': no_result,
    }
    template = 'search/result-view.html'
    if request.htmx:
        context['articles']= found_articles[:3]
        context['recipes']= found_recipes[:3]
        template = 'search/partials/par-result.html'
    return render(request, template, context=context)
