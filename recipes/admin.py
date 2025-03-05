from django.contrib import admin
from .models import Recipe, RecipeIngredients, RecipeImage

# Register your models here.

admin.site.register(RecipeImage)

class RecipeIngredientsInLine(admin.StackedInline):
    model = RecipeIngredients
    exclude = ['float_qty']
    readonly_fields = ['to_metric', 'to_imperial']
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInLine]
    list_display = ['name', 'user']
    readonly_fields = ['created', 'updated', 'slug']
    raw_id_fields = ['user']

class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'recipe_name']
    exclude = ['float_qty']
    readonly_fields = ['to_metric', 'to_imperial']


admin.site.register(RecipeIngredients, RecipeIngredientsAdmin)
admin.site.register(Recipe, RecipeAdmin)