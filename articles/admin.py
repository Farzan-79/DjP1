from django.contrib import admin

# Register your models here.

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'id', 'created', 'updated', 'publish']
    search_fields = ['title', 'content', 'id']
    raw_id_fields = ['user']
    readonly_fields= ['slug']
    
admin.site.register(Article, ArticleAdmin)