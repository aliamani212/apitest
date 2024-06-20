from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.blog.models import Article
from apps.blog.serializer import ArticleSerializer, CreateArticleSerializer
from utility.utils import get_response
from drf_spectacular.utils import extend_schema, OpenApiParameter


# Create your views here.
class ArticleList(APIView):
    @extend_schema(
        request=ArticleSerializer,
        responses={
            status.HTTP_200_OK: ArticleSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: 'مقاله یافت نشد',
            status.HTTP_500_INTERNAL_SERVER_ERROR: 'کد ارور داره'
        },
    )
    def get(self, request):
        result = Article.objects.all()
        result_ser = ArticleSerializer(result, many=True)
        return Response(get_response(status.HTTP_200_OK, result_ser.data, 'کلیه مقالات'))


class ArticleById(APIView):
    @extend_schema(
        request=ArticleSerializer,
        responses={
            status.HTTP_200_OK: ArticleSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: 'مقاله یافت نشد',
            status.HTTP_500_INTERNAL_SERVER_ERROR: 'کد ارور داره'
        },
    )
    def get(self, request, id: int):
        try:
            article = Article.objects.get(id=id)
            article_ser = ArticleSerializer(article)
            return Response(get_response(status.HTTP_200_OK, article_ser.data, 'بر اساس آی دی'))
        except:
            return Response(get_response(status.HTTP_400_BAD_REQUEST, None, 'مقاله یافت نشد'))


class CreateArticle(APIView):
    @extend_schema(
        request=CreateArticleSerializer,
        responses={
            status.HTTP_200_OK: ArticleSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: 'مقاله یافت نشد',
            status.HTTP_500_INTERNAL_SERVER_ERROR: 'کد ارور داره'
        },
    )
    def post(self, request):
        article_ser = CreateArticleSerializer(data=request.data,partial=True)
        if article_ser.is_valid():
            article_ser.save()
            return Response(get_response(status.HTTP_201_CREATED, article_ser.data, 'مقاله ایجاد شد'))
        else:
            return Response(get_response(status.HTTP_400_BAD_REQUEST, None, 'مقاله ایجاد نشد'))
