from django.db import models
from django.conf import settings


from .validators import validate_unit, validate_qty
from .utils import valid_unit, valid_qty
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='recipe')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null= True)
    directions = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ings')
    name = models.CharField(max_length= 200)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50, validators=[validate_qty])
    unit = models.CharField(max_length=50, validators=[validate_unit])
    directions = models.TextField(blank= True, null= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def cleaned_qty_unit(self):
        self.quantity = valid_qty(self.quantity)
        self.unit = valid_unit(self.unit)
        
    

    def save(self, *args, **kwargs):
        self.cleaned_qty_unit()
        super().save(*args, **kwargs)

    def recipe_name(self):
        return self.recipe.name
    
class RecipeIngredientImage(models.Model):
    ingredient = models.ForeignKey(RecipeIngredients, on_delete=models.CASCADE, related_name='image')
    name = models.CharField(max_length=100)