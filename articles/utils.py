from django.utils.text import slugify

def slugify_article_instance(instance, save=False):
    slug = slugify(instance.title)
    uslug = slug
    n = 1
    Klass = instance.__class__
    while Klass.objects.filter(slug__startswith=uslug).exclude(id=instance.id).exists():
        uslug = f'{slug}-{n}'
        n += 1
    instance.slug = uslug
    instance.save()