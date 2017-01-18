# events/urls.py

from django.conf.urls import url
from .views import ArticleDetailView, event_list, past_events, EventDetailView


urlpatterns = [
	url(r'^$', event_list),
	url(r'^past/', past_events, name="past_events"),
	url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view()),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 
        EventDetailView.as_view()),
]


