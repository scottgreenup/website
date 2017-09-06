from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    timestamp = models.DateTimeField('date published')
    author = models.CharField(max_length=256)
    content = models.TextField()
