from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleManageAPIView.as_view(), name='article_manage'),
    path('<int:id>', views.ArticleManageAPIView.as_view(), name='article_manage_by_id'),
    path('add/', views.ArticleManageAPIView.as_view(), name='add_article'),

]
