from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from articles.forms import ArticleForm
from articles.models import Article

# Create your views here.
def article_search(request):
    #print(request.GET)
    query_dict = request.GET # this is a dictionary of all of the queries
    query = query_dict.get('q')
    article_object = None
    print(query)
    context ={
        'object' : article_object,
        'q' : query,
        }
    if query is not None:
        try:
            article_object = Article.objects.get(id=query)
            context ={
                'object' : article_object,
                'q' : query,
                }
        except Article.DoesNotExist:
            return render(request, 'articles/no-resault.html', context=context)


    return render(request, 'articles/detail.html', context=context)
    


def articles_detail_view(request, slug=None):
    #article_obj = None
    
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            return render(request, 'error404.html',{'object_list': Article.objects.all()})

    context = {
        'object' : article_obj,
        'object_list': Article.objects.all()
    }

    return render(request, 'articles/detail.html', context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        article_object = form.save()
        #title = form.cleaned_data.get('title')
        #content = form.cleaned_data.get('content')
        ## print(title,content)
        #article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    return render(request, 'articles/create.html', context=context)