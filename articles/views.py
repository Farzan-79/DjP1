from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from articles.forms import ArticleForm
from articles.models import Article

# Create your views here.
def article_search(request):
    query = request.GET.get('q')
    context = {
        'object_list': Article.objects.none(),
        'query': query,
        'no_resault': False,
        'too_short': False
    }
    if query is not None:
        if len(query) < 2:
            context['too_short'] = True
        else:
            qs = Article.objects.search(query= query)
            if qs.exists():
                context['object_list']= qs
            else:
                context['no_resault']= True
    
    return render(request, 'articles/search.html', context=context)

    #if query is not None and len(query) >= 2:
    #        qs = Article.objects.search(query)
    #        if qs.exists():
    #            context['object_list']= qs
    #        else:
    #            context['no_resault'] = True
    #    elif query is not None and len(query) < 2:
    #        context['too_short'] = True
    #
    #    return render(request, 'articles/search.html', context=context)
    


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