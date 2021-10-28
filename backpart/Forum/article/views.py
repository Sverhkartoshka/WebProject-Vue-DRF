from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Author, Comment
from .serializers import ArticleSerializer, AuthorSerializer, CommentSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all().order_by('-id')
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        print('\n1 ', article, '\n')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, 
                     partial=True)
        
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({
            "success": "Article '{}' updated successfully".format(article_saved.title)
        })
    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Article with id `{}` has been deleted".format(pk)
        }, status=204)

class LogView(APIView):
    def post(self, request):
        author = request.data.get('author')
        if Author.objects.filter(name = author["name"]).exists():
            usercheck = get_object_or_404(Author.objects.all(), name=author["name"])
            if (usercheck.password == author["password"]):
                return Response("OK")
            else:
                return Response("NoPass")
        else:
            return Response("NoUser")

class RegView(APIView):
    def post(self, request):
        author = request.data.get('author')
        serializer = AuthorSerializer(data=author)
        if Author.objects.filter(name = author["name"]).exists():
            return Response(False)
        else:
            if serializer.is_valid(raise_exception=True):
                author_saved = serializer.save()
            return Response(True)

class FetchCommentsView(APIView):
    def get(self, request, postid):
        comments = Comment.objects.filter(assigned=postid).order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response({"comments": serializer.data})

    def post(self, request):
        comment = request.data.get('comment_add')
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
        return Response({"success": True})
        
    def delete(self, request, pk):
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        comment.delete()
        return Response({
            "message": "Comment with id `{}` has been deleted".format(pk)
        }, status=204)