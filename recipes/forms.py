from django import forms
from recipes.models import RecipeIngredients, Recipe

class RecipeCreateNameForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Recipe.objects.filter(name__iexact = name)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(f'a recipe with {name} as name already exists')
        return name
    
class RecipeCreateDetailsForm(forms.ModelForm):
    pass



class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required_field'
    #name = forms.CharField(widget= forms.TextInput(attrs= {"placeholder": "Recipe name", "class": "m-3"}))
    #description = forms.CharField(widget= forms.Textarea(attrs={"placeholder": "describe the food in a nutshel", "rows": "2"}))
    #directions = forms.CharField(widget= forms.Textarea(attrs={"placeholder": "explain the steps", "rows": "4"}))
    class Meta:
        model = Recipe
        fields = ['name','description', 'directions']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({"placeholder": "Recipe name"})
        self.fields['description'].widget.attrs.update({"placeholder": "describe the food in a nutshel", "rows": "2"})
        self.fields['directions'].widget.attrs.update({"placeholder": "explain the steps", "rows": "4"})

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
        #if self.instance:
        #    if (name == self.instance.name and
        #        description == self.instance.description and
        #        directions == self.instance.directions):
        #        raise forms.ValidationError('you haven\'t change anything')
        return cleaned_data
    
class RecipeIngredientsForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required_field'
    class Meta:
        model = RecipeIngredients
        fields = ['name', 'quantity', 'unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            new_attrs={
                "placeholder": f'Ingredient\'s {field}',
                # i should learn more about these below...
                # "class": 'form-control',
                # "hx-post": ".",
                # "hx-trigger": "keyup changed delay:500ms",
                # "hx-target": "#recipe-container",
                # "hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(new_attrs)


