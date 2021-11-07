from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
# DEFINES THE MODEL
class Post(models.Model):
    title = models.CharField(max_legnth=200)
    artist = models.ForignKey(settings.Auth_USER_MODEL, on_delete=models.CASCADE)
#  The `created_at` field should reflect the time that the album object is created (not the year that the album was released,
    created_at = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title