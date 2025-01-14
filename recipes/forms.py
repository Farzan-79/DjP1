from django import forms
from recipes.models import RecipeIngredients, Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def clean_title(self):
        name = self.cleaned_data.get('name')
        id = self.cleaned_data.get('id')
        qs = Recipe.objects.filter(name__iexact = name).exclude(id= id)
        if qs.exists():
            raise forms.ValidationError(f'a recipe with {name} as name already exists')
        return name