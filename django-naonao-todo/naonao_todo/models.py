
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title
