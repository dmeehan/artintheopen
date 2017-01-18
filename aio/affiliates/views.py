# affilates/views.py

#from django.views.generic.list_detail import object_list, object_detail
from django.views.generic import DetailView, ListView
from cms.models import SectionArticleRelation
from cms.models import Article
from affiliates.models import Affiliate
from events.models import Event

class AffiliateDetailView(DetailView):

    model = Affiliate

class AffiliateIndexView(ListView):

    model = Affiliate
    template_name='affiliates/affiliate_index.html'

    def get_context_data(self, **kwargs):
        context = super(AffiliateIndexView, self).get_context_data(**kwargs)
        items = SectionArticleRelation.objects.filter(section__name__iexact="affiliates").filter(article__status=1)
        events = Event.future.filter(aio=False).filter(affiliate__isnull=False)
        upcoming = Event.upcoming.filter(aio=False).filter(affiliate__isnull=False)
        sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="affiliates").filter(article__status=1).order_by('section__parent__name')
        context['sub_items'] = sub_items
        context['items'] = items
        context['events'] = events
        context['upcoming'] = upcoming
        context['sub_items'] = sub_items
        return context


#def affiliate_index(request):
#    items = SectionArticleRelation.objects.filter(section__name__iexact="affiliates").filter(article__status=1)
#    affiliates = Affiliate.objects.all()
#    events = Event.future.filter(aio=False).filter(affiliate__isnull=False)
#    upcoming = Event.upcoming.filter(aio=False).filter(affiliate__isnull=False)
#    sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="affiliates").filter(article__status=1).order_by('section__parent__name')
#    return object_list(request, queryset=affiliates,
#                       template_name = 'affiliates/affiliate_index.html',
#                       extra_context={'items': items,
#                                      'sub_items': sub_items, 
#                                      'events': events,
#		                      'upcoming': upcoming })
 

class ArticleDetailView(DetailView):

    queryset = Article.live.all()
    template_object_name='article'
    template_name = 'affiliates/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="affiliates").filter(article__status=1).order_by('section__parent__name')
        context['sub_items'] = sub_items
        return context                                     
  


#def article_detail(request, slug):
#    articles = Article.live.all()
#    sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="affiliates").filter(article__status=1).order_by('section__parent__name')
#    return object_detail(request, queryset=articles,
#                         slug=slug, slug_field='slug',
#                         template_name = 'affiliates/article_detail.html',
#                         template_object_name='article',
#                         extra_context={'affiliates': Affiliate.objects.all,
#                                        'sub_items': sub_items, })
