# artists/urls.py

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .models import Artist
from .views import ArtistIndexView, ArtistInfoView, ArtistDetailView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArtistIndexView.as_view()),
    url(r'^participants/info/$', login_required(ArtistInfoView.as_view()), name="artist_info"),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view()),
    url(r'^aio/(?P<slug>[-\w]+)/$', ArtistDetailView.as_view(), name="artist_detail"),
]
