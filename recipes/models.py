from pathlib import Path
import time
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from articles.utils import slugify_article_instance
from django.urls import reverse
import pint
from django.core.exceptions import ValidationError
from django.db.models import Q


from .validators import validate_unit, validate_qty
from .utils import valid_unit, valid_qty
# Create your models here.

class RecipeQuerySet(models.QuerySet):
    def search(self, query= None):
        if query is None or query == "":
            return self.none()
        lookups = Q(name__icontains= query) | Q(description__icontains= query)
        return self.filter(lookups)

class RecipeManager(models.Manager):
    def get_queryset(self):
        return RecipeQuerySet(self.model, using=self._db)
    
    def search(self, query= None):
        return self.get_queryset().search(query= query)


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='recipe')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null= True)
    directions = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank= True, null= True)

    objects = RecipeManager()

    def save(self, *args, **kwargs):
        if self.slug is None or not self.slug.startswith(slugify(self.name)):
            slugify_article_instance(self)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs= {'slug': self.slug})
    
    def get_hx_url(self): #the partial
        return reverse('recipes:hx-detail', kwargs= {'slug': self.slug})
    
    def get_update_url(self):
        return reverse('recipes:update', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('recipes:delete', kwargs={'slug': self.slug})




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

    def get_absolute_url(self): #of its recipe
        return self.recipe.get_absolute_url()
    
    def get_delete_url(self):
        return reverse('recipes:ing-delete', kwargs={'parent_slug':self.recipe.slug, 'id':self.id})
        
    def get_hx_update_url(self): # of the form that will edit this instance
        return reverse('recipes:hx-ing-update', kwargs={'parent_slug':self.recipe.slug, 'id':self.id})
        
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


def recipe_image_upload_handler(instance, filename):
    fpath = Path(filename)
    ext = fpath.suffix  # Includes the dot, e.g. ".jpg"
    clean_name = fpath.stem  # Filename without extension
    
    # Create organized path structure
    path = Path("recipes") / f"recipe_{instance.recipe.slug}"
    
    # Final filename: originalname_timestamp.ext
    new_filename = f"{clean_name}_{int(time.time())}{ext}"
    
    return str(path / new_filename)

class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='image')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=recipe_image_upload_handler)

