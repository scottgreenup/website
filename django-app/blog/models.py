from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('last updated')
    author = models.CharField(max_length=256)
    content = models.TextField()
