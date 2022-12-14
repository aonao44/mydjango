from pickle import FALSE
from unicodedata import category
from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリー', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='tag', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=200)
    content = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)
    is_published = models.BooleanField(verbose_name='公開設定', default=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True)

    tag = models.ManyToManyField(
        Tag,
        verbose_name='tag',
        blank=True
    )

    def __str__(self):
        return self.title
