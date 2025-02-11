from django.urls import path

from .views import (
    recipe_create_view,
    recipe_detail_view,
    recipe_update_view,
    recipes_view,
    recipe_detail_hx_view
)

app_name = 'recipes'
urlpatterns=[
    path('', recipes_view, name= 'list'),
    path('create/', recipe_create_view, name= 'create'),
    path('hx/<slug:slug>', recipe_detail_hx_view, name='hx-detail'),
    path('<slug:slug>/update/', recipe_update_view, name= 'update'),
    path('<slug:slug>/', recipe_detail_view, name= 'detail')
]