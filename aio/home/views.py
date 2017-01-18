# home/views.py

from django.shortcuts import get_list_or_404, render
from django.views.generic import DetailView, ListView
from django.template import RequestContext


from cms.models import SectionArticleRelation, Article
from artists.models import Artist
from events.models import Event
from affiliates.models import Affiliate


class IndexView(ListView):
    queryset = Artist.live.filter(featured_home=True)
    template_object_name='artists'
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        items = SectionArticleRelation.objects.filter(section__name__iexact="home").filter(article__status=1)
        featured_events = Event.featured.all()
        upcoming_events = Event.future.all()[:1]
        affiliates = Affiliate.home_feature.all()
        context['items'] = items
        context['featured_events'] = featured_events
        context['upcoming_events'] = upcoming_events
        context['affiliates'] = affiliates
        return context  

#def index(request):
#    items = SectionArticleRelation.objects.filter(section__name__iexact="home").filter(article__status=1)
#    artists = Artist.live.filter(featured_home=True)
#    featured_events = Event.featured.all()
#    upcoming_events = Event.future.all()[:1]
#    affiliates = Affiliate.home_feature.all()
#    return render(request, 'home/index.html',
#                              {'items': items,
#                               'artists': artists,
#                               'featured_events': featured_events,
#                               'upcoming_events': upcoming_events,
#                               'affiliates': affiliates })
                               
#def article_detail(request, slug):
#    articles = Article.live.all()
#    artists = Artist.live.filter(featured_home=True)
#    featured_events = Event.home_feature.order_by('start_date')
#    upcoming_events = Event.upcoming.all()
#    affiliates = Affiliate.home_feature.all()
#    return object_detail(request, queryset=articles,
#                        slug=slug, slug_field='slug',
#                         template_name = 'home/article_detail.html',
#                         template_object_name='article',
#                         extra_context={'artists': artists,
#                                        'featured_events': featured_events,
#                                        'upcoming_events': upcoming_events,
#                                        'affiliates': affiliates, })


class ArticleDetailView(DetailView):

    queryset = Article.live.all()
    template_object_name='article'
    template_name = 'home/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        artists = Artist.live.filter(featured_home=True)
        featured_events = Event.home_feature.order_by('start_date')
        upcoming_events = Event.upcoming.all()
        affiliates = Affiliate.home_feature.all()
        context['artists'] = artists
        context['featured_events'] = featured_events
        context['upcoming_events'] = upcoming_events
        context['affiliates'] = affiliates
        return context    

