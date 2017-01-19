# home/urls.py

from django.conf.urls import url
from .views import ArticleDetailView, IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^home/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name="home_article_detail"),
]