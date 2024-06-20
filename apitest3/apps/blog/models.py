from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=200)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover = models.ImageField(upload_to='articles/', blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def get_cover(self):
        return mark_safe('<img src="/media/%s" width="100" height="100">' % self.cover)
