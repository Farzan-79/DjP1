from django.urls import path

from .views import (
    recipe_create_view,
    recipe_detail_view,
    recipe_update_view,
    recipes_view,
    recipe_detail_hx_view,
    ingredient_update_view,
    recipe_delete_view,
    recipe_ingredient_delete_view,
    recipe_image_upload_view,
)

app_name = 'recipes'
urlpatterns=[
    path('', recipes_view, name= 'list'),
    path('create/', recipe_create_view, name= 'create'),

    path('hx/<slug:parent_slug>/ing_update/<int:id>/', ingredient_update_view, name='hx-ing-update'),
    path('hx/<slug:parent_slug>/ing_update/', ingredient_update_view, name='hx-ing-create'),
    path('hx/<slug:slug>/', recipe_detail_hx_view, name='hx-detail'),
    path('hx/<slug:parent_slug>/image-upload/', recipe_image_upload_view, name='hx-image-upload'),


    path('<slug:parent_slug>/image-upload/', recipe_image_upload_view, name='image-upload'),
    path('<slug:parent_slug>/ing_delete/<int:id>/', recipe_ingredient_delete_view, name='ing-delete'),    
    path('<slug:slug>/delete/', recipe_delete_view, name='delete'),
    path('<slug:slug>/update/', recipe_update_view, name= 'update'),
    path('<slug:slug>/', recipe_detail_view, name= 'detail'),
]