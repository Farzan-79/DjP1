from django.db import models
import django.utils.timezone
from django.db.models.signals import pre_save, post_save
from .utils import slugify_article_instance
from django.utils.text import slugify
from django.urls import reverse
from django.db.models import Q

from django.conf import settings
# Create your models here.

class ArticleQuerySet(models.QuerySet):
    def search(self, query= None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains= query) | Q(content__icontains= query)
        return self.filter(lookups)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    
    def search(self, query= None):
        return self.get_queryset().search(query= query)

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    objects = ArticleManager()

    def get_absolute_urls(self):
        #return f'/articles/{self.slug}'
        return reverse('articles:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug is None or not self.slug.startswith(slugify(self.title)):
            slugify_article_instance(self)
        super().save(*args, **kwargs)




#def article_pre_save(sender, instance, *args, **kwargs):
#    print('pre save')
#    
#
#pre_save.connect(article_pre_save, sender=Article)

#def article_post_save(sender, instance, created, *args, **kwargs):
#    print('post save')
#    if created:
#        slugify_article_instance(instance, save=True)

#post_save.connect(article_post_save, sender=Article)