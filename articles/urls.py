from django.urls import path

from .views import (
    article_create_view,
    article_view,
    articles_detail_view,
    artice_update_view,
    article_delete_view
)

app_name= 'articles'
urlpatterns= [
    path('', article_view, name= 'list'),
    path('create/', article_create_view, name= 'create'),
    path('<slug:slug>/update/', artice_update_view, name='update'),
    path('<slug:slug>/delete/', article_delete_view, name='delete'),
    path('<slug:slug>/', articles_detail_view, name= 'detail'),
]