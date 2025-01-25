from django import forms
from recipes.models import RecipeIngredients, Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Recipe.objects.filter(name__iexact = name)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(f'a recipe with {name} as name already exists')
        return name
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        directions = cleaned_data.get('directions')
        if self.instance:
            if (name == self.instance.name and
                description == self.instance.description and
                directions == self.instance.directions):
                raise forms.ValidationError('you haven\'t changed anything')
        return cleaned_data
