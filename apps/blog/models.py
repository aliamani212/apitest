from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(upload_to='article_cover')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles_author')
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="articles_category")

    def getCover(self):
        return mark_safe('<img src="/media/%s" width=100 height=50 /> ' % self.cover)
