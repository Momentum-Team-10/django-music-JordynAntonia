from django.contrib import admin
from .models import Artist, Entry, Post, Site
# Register your models here.

admin.site.register(Post)
admin.site.register(Artist)
admin.site.register(Entry)
admin.site.register(Site)
