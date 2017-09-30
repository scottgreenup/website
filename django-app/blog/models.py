from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(
        'date published',
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        'last updated',
        default=timezone.now
    )
    author = models.CharField(max_length=256)
    content = models.TextField()
