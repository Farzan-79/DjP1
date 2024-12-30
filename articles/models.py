from django.db import models
import django.utils.timezone
from django.db.models.signals import pre_save, post_save
from .utils import slugify_article_instance

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    print('pre save')
    if instance.slug is None:
        slugify_article_instance(instance)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    print('post save')
    if created:
        slugify_article_instance(instance, save=True)

post_save.connect(article_post_save, sender=Article)