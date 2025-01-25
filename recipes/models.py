from django.db import models
from django.conf import settings
from django.utils.text import slugify
from articles.utils import slugify_article_instance
from django.urls import reverse
import pint
from django.core.exceptions import ValidationError


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
    slug = models.SlugField(unique=True, blank= True, null= True)

    def save(self, *args, **kwargs):
        if self.slug is None or not self.slug.startswith(slugify(self.name)):
            slugify_article_instance(self)
        super().save(*args, **kwargs)

    def get_absolute_urls(self):
        return reverse('recipes:detail', kwargs= {'slug': self.slug})



class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ings')
    name = models.CharField(max_length= 200)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50, validators=[validate_qty])
    unit = models.CharField(max_length=50, validators=[validate_unit])
    float_qty = models.FloatField(blank=True, null=True)
    directions = models.TextField(blank= True, null= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
        
    def convert_units(self, system= 'mks'):
        if self.float_qty is None:
            return None
        ureg = pint.UnitRegistry(system= system)
        measurement = self.float_qty * ureg[self.unit]
        return measurement

    def to_metric(self):
        measurement = self.convert_units(system= 'mks')
        return measurement.to_base_units()
    
    def to_imperial(self):
        measurement = self.convert_units(system= 'imperial')
        return measurement.to_base_units()
    
    def cleaned_qty_unit(self):
        self.quantity = valid_qty(self.quantity)
        self.unit = valid_unit(self.unit)
        self.float_qty = valid_qty(self.quantity)
        if self.float_qty is None:
            raise ValidationError('float qty is None')

    def save(self, *args, **kwargs):
        self.cleaned_qty_unit()
        super().save(*args, **kwargs)

    def recipe_name(self):
        return self.recipe.name
    
class RecipeIngredientImage(models.Model):
    ingredient = models.ForeignKey(RecipeIngredients, on_delete=models.CASCADE, related_name='image')
    name = models.CharField(max_length=100)