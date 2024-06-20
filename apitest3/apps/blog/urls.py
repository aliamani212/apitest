from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('<int:id>', views.ArticleById.as_view()),
    path('add/', views.CreateArticle.as_view()),
]
