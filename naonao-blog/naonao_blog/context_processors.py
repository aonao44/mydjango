import collections
from unicodedata import category
from django.db.models import Count, Q

from naonao_blog.models import Category, Tag, Post


def common(request):
    context = {
        'categories': Category.objects.annotate(
            count=Count('post', Q(post__is_published=True))
        ),
        'tags': Tag.objects.all(),
        'posts': Post.objects.all(),
    }

    return context
