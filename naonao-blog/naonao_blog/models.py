from distutils.command.upload import upload
from turtle import title
from venv import create
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='CATEGORY', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='TAG', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    content = models.TextField(verbose_name='CONTENT')
    image = models.ImageField(verbose_name='IMAGE', upload_to='uploads/', null=True, blank=True)
    created_at = models.DateField(verbose_name='CREATED', auto_now_add=True)
    updated_at = models.DateField(verbose_name='UPDATED', auto_now=True)
    is_published = models.BooleanField(verbose_name='PUBLISHEING')

    category = models.ForeignKey(
        Category, verbose_name='CATEGORY', on_delete=models.PROTECT, null=True, blank=True)

    tag = models.ManyToManyField(
        Tag, verbose_name='TAG',  blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    name = models.CharField(verbose_name='NAME', max_length=100)
    text = models.TextField(verbose_name='TEXT')
    created_at = models.DateTimeField(verbose_name='CREATE', auto_now=False, auto_now_add=True)

    post = models.ForeignKey(Post, verbose_name='POST', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]


class Reply(models.Model):
    name = models.CharField(verbose_name='NAME', max_length=100)
    text = models.TextField(verbose_name='TEXT')
    created_at = models.DateTimeField(verbose_name='CREATE', auto_now=False, auto_now_add=True)

    comment = models.ForeignKey(Comment, verbose_name='COMMNET', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]
