from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.TextField(default="No title")
    cover = models.ImageField(upload_to='images/')
    caption = models.TextField(default="No description")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        string = self.title + ": " + self.caption
        return string

    def get_absolute_url(self):
        # 'reverse()' will return full path as a string
        return reverse('post-detail', kwargs={'pk': self.pk})


class ListAdmin(admin.ModelAdmin):
    field = ('title', 'cover', 'caption', 'author')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
