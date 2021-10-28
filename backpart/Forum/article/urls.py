from django.urls import path

from .views import ArticleView, LogView, RegView, FetchCommentsView

app_name = "articles"

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
    path('authors/log/', LogView.as_view()),
    path('authors/reg/', RegView.as_view()),
    path('comments/', FetchCommentsView.as_view()),
    path('comments/<int:postid>', FetchCommentsView.as_view()),
    path('comments/<int:pk>', FetchCommentsView.as_view()),
]