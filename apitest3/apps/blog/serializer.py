from rest_framework import serializers
from .models import Category, Article
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'cover', 'category', 'created_at', 'user']


class CreateArticleSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=True, use_url=True, max_length=None)

    class Meta:
        model = Article
        fields = ['title', 'content', 'cover', 'category', 'user']
