from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
# DEFINES THE MODEL
class Post(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def create(self):
        self.created_at = timezone.now()
        self.save()
    
    def __str__(self):
        # A Python “magic method” that returns a string representation of any object.
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)


    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    post = models.ForignKey(Post, on_delete=models.CASCADE)
    album = models.ManyToManyField(Album)
    title = models.CharField(max_legnth=200)
    artist = models.ManyToManyField(Artist)
    created_at = models.DateTimeField(default=timezone.now)
    data = models.JSONField(null=True)


    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=300)
    entries = models.ManyToManyField(Entry)

    def __str__(self):
        return self.name
