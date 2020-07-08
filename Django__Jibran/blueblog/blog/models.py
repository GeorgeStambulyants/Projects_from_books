from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    owner = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, editable=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.title)


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, editable=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.title)
