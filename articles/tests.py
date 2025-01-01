from django.test import TestCase
from .models import Article
from .utils import slugify_article_instance
from django.utils.text import slugify
# Create your tests here.

class ArticleTestCase(TestCase):

    def setUp(self):
        self.number = 100
        for obj in range(0,self.number):
            Article.objects.create(title=f"hi", content = "hello")
        
    def test_article_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number, f"wrong, its {qs.count()}")#f"number of articles ar not 5, but {qs.count()}")

    def test_unique_slug(self):
        qs = Article.objects.all().values_list('slug', flat=True)
        slugs = []
        for s in qs:
            slugs.append(s)
        ns = list(set(slugs))
        self.assertEqual(len(slugs), len(ns))


    def test_hello(self):
        obj = Article.objects.all().order_by('id')[0]
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)