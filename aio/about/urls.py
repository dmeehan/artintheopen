# about/urls.py

from django.conf.urls import *
from cms.models import *

from django.conf.urls import url

from .views import about_index, ArticleDetailView
urlpatterns = [
    url(r'^$', about_index),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view()),
]
