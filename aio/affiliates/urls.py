# affiliates/urls.py

from django.conf.urls import url

from .models import Affiliate
from .views import ArticleDetailView, AffiliateIndexView, AffiliateDetailView

affiliate_info_dict = {
  'queryset': Affiliate.objects.all(),
}

urlpatterns = [
	url(r'^$', AffiliateIndexView.as_view()),
	url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name="affiliates_article_detail"),
	url(r'^(?P<level>[-\w]+)/(?P<slug>[-\w]+)/$', 
        AffiliateDetailView.as_view, name='affilate_detail'),
]
