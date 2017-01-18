# about/views.py

#from django.views.generic.list_detail import object_detail
from django.views.generic import DetailView
from django.shortcuts import render
from django.template import RequestContext

from cms.models import SectionArticleRelation
from cms.models import Article
from events.models import Event

def about_index(request):
    events = Event.local.all()
    items = SectionArticleRelation.objects.filter(section__name__iexact="about").filter(article__status=1)
    sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="about").filter(article__status=1).order_by('section__parent__name')
    return render(request,'about/about.html',
                              {'items': items,
                               'sub_items': sub_items,
                               'events': events, })

#def article_detail(request, slug):
#    articles = Article.live.all()
#    sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="about").filter(article__status=1).order_by('section__parent__name')
#    return object_detail(request, queryset=articles,
#                         slug=slug, slug_field='slug',
#                         template_name='about/article_detail.html',
#                         template_object_name='article',
#                         extra_context={'sub_items':sub_items})


class ArticleDetailView(DetailView):

    queryset = Article.live.all()
    template_object_name='article'
    template_name='about/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="about").filter(article__status=1).order_by('section__parent__name')
        context['sub_items'] = sub_items
        return context
