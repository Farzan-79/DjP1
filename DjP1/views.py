from django.http import HttpResponse
import random
from django.template.loader import render_to_string
from articles.models import Article
from django.shortcuts import render
from django.conf import settings


def home_view(request,*args, **kwargs):
    #random_number = random.randint(1,100)
    ##print(f'this is args: {args}, and this is kwargs: {kwargs}')
    #try:
    #    article_queryset = Article.objects.all()
    #    random_id = random.randint(6,9)
    #    article_object = Article.objects.get(id=random_id)
#
    #    context = { 
    #        #'title': article_object.title,
    #        #'content': article_object.content,
    #        #'id': article_object.id,
    #        'object' : article_object,
    #        'number': random_number,
    #        'object_list': article_queryset,
    #    }

        HTML_STRING = render_to_string('home-view.html', context={})
        return HttpResponse(HTML_STRING)
    #except Article.DoesNotExist:
    #    context = {'object_list': article_queryset}
    #    #error404 = render_to_string('error404.html', context=context)
    #    #return HttpResponse(error404)
    #    return render(request, "error404.html", context=context)
    #    
   
    
           
            #    HTML_STRING = '''
            #<h1>{title}!</h1>
            #<h1>{content} (id={id})</h1>
            #and this is the first webpage that i\'ve ever made :) {number}
            #'''.format(**context_with_number)

    

def wrong_view(request):
    SCARY_STRING = '''
<h1>DO NOT TYPE THIS SHIT THAT'S ILLEGAL</h1>
'''
    return HttpResponse(SCARY_STRING)


#article_queryset = Article.objects.all()


#def home_view(request):
#    error404 = render_to_string('error404.html', context=context)
#
#    x = random.randint(6,9)
#    try:
#        article_obj = Article.objects.get(id=x)
#    except Article.DoesNotExist:
#        return HttpResponse(error404)
#    
#    context = {
#        'object_list' : article_queryset,
#        'title' : article_obj.title,
#        'content' : article_obj.content,
#        'id' : article_obj.id,
#        'number': random.randint(1,101)
#    }
#    HTML_STRING = render_to_string('home-view.html', context= context)
#    
#
#    return HttpResponse(HTML_STRING)