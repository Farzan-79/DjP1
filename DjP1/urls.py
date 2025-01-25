"""
URL configuration for DjP1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import (
    home_view,
    wrong_view
)
#from articles.views import (
#    article_search,
#    article_create_view,
#    articles_detail_view,
#)
from accounts.views import(
    login_view,
    logout_view,
    register_view,
)

#from recipes.views import(
#    recipes_view,
#    recipe_detail_view,
#    recipe_create_view,
#    recipe_update_view
#)
urlpatterns = [
    path('pantry/recipes/', include('recipes.urls')),
    path('pantry/articles/', include('articles.urls')),
    path('', home_view, name='home'),
    #path('articles/', article_search, name='articles'),
    #path('create/', article_create_view),  # Move this above the slug path
    #path('articles/<slug:slug>/', articles_detail_view, name='article-detail'),
    path('fu', wrong_view),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    #path('recipes/', recipes_view, name='recipes'),
    #path('recipes/create/', recipe_create_view, name='recipe-create'),
    #path('recipes/<slug:slug>/', recipe_detail_view, name='recipe-detail'),
    #path('recipes/<slug:slug>/update', recipe_update_view, name='recipe-update')
    #path('recipes/', recipe_view, name='recipes'),
]