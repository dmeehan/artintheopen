# events/views.py

from django.shortcuts import get_list_or_404, render
from django.views.generic import DetailView
from django.views.generic.dates import DateDetailView
from django.template import RequestContext

from cms.models import SectionArticleRelation, Article
from .models import Event

def event_list(request):
    items = SectionArticleRelation.objects.filter(section__name__iexact="Events").filter(article__status=1)
    events = Event.future.all()
    past_events = Event.past.all()
    aio_events = Event.local.all()
    upcoming_events = Event.upcoming.all()
    return render(request, 'events/event_list.html',
                              {'items': items,
                               'events': events,
                               'past_events': past_events,
                               'upcoming_events': upcoming_events,
                               'aio_events': aio_events, })


#def article_detail(request, slug):
#    articles = Article.live.all()
#    sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="events").filter(article__status=1).order_by('section__parent__name')
#    return object_detail(request, queryset=articles,
#                         slug=slug, slug_field='slug',
#                         template_name = 'events/article_detail.html',
#                         template_object_name='article',
#                         extra_context={'events': Event.future.all,
#                                        'sub_items': sub_items, })
   
class ArticleDetailView(DetailView):

    queryset = Article.live.all()
    template_object_name='article'
    template_name = 'events/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="events").filter(article__status=1).order_by('section__parent__name')
        context['sub_items'] = sub_items
        return context                                     
                                        

def past_events(request):
    events = Event.past.all()
    aio_events = Event.local_past.all()
    return render(request, 'events/event_list.html',
                              {'events': events,
                               'aio_events': aio_events, })


class EventDetailView(DateDetailView):
    model = Event
    date_field ='start_date'
    slug_field ='slug'
    template_object_name = 'event'
    allow_future = True

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        events = Event.future.all(),
        context['events'] = events
        return context 
  