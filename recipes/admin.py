from django.contrib import admin
from .models import Recipe, RecipeIngredients

# Register your models here.

class RecipeIngredientsInLine(admin.StackedInline):
    model = RecipeIngredients
    #fields = ['name', 'unit', 'quantity', 'directions']
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInLine]
    list_display = ['name', 'user']
    readonly_fields = ['created', 'updated']
    raw_id_fields = ['user']

class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'recipe_name']
    readonly_fields = ['float_quantity']


admin.site.register(RecipeIngredients, RecipeIngredientsAdmin)
admin.site.register(Recipe, RecipeAdmin)