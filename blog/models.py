from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('p', 'Publish'),
        ('d', 'Draft'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    def __str__(self) -> str:
        return self.title