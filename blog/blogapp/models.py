from tkinter.tix import Tree
from django.db import models

# Create your models here.


class Post(models.Model):
    """Model definition for Post."""
    title = models.CharField(verbose_name='title', max_length=200)
    content = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(verbose_name='created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='update', auto_now=True)
    is_published = models.BooleanField(verbose_name='published')

    # TODO: Define fields here

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title
