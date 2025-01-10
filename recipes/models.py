from django.db import models
from django.conf import settings

from .utils import str_to_float
from .validators import validate_unit
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
    quantity = models.CharField(max_length=50)
    float_quantity = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators =[validate_unit])
    directions = models.TextField(blank= True, null= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        qty = self.quantity
        float_qty , success = str_to_float(qty)
        if success:
            self.float_quantity = float_qty
        else:
            self.float_quantity = None
        super().save(*args, **kwargs)

    def recipe_name(self):
        return self.recipe.name
    
class RecipeIngredientImage(models.Model):
    ingredient = models.ForeignKey(RecipeIngredients, on_delete=models.CASCADE, related_name='image')
    name = models.CharField(max_length=100)