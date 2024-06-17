from .serializer import ArticleSerializer, CreateArticleSerializer
from .models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema


class ArticleManageAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                article = Article.objects.get(id=id)
                serializer = ArticleSerializer(article)
                return Response(serializer.data)
            except Article.DoesNotExist:
                return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'article not found'})
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

    @extend_schema(
        request=CreateArticleSerializer,
        responses={200: ArticleSerializer()}
    )
    def post(self, request):
        article_serialize = CreateArticleSerializer(request.POST)
        if article_serialize.is_valid():
            article = article_serialize.save()
            res = ArticleSerializer(article)
            return Response(res.data)
