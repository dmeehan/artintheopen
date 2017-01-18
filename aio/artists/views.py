# artists/views.py

from django.contrib.auth.decorators import login_required
#from django.views.generic.list_detail import object_list, object_detail
#rom django.views.generic.list_detail import object_detail
from django.views.generic import DetailView, ListView

from cms.models import SectionArticleRelation
from cms.models import Article
from .models import Artist


class ArtistIndexView(ListView):

    queryset = Artist.live.all()
    template_object_name ='artist'
    template_name ='artists/artists_index.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistIndexView, self).get_context_data(**kwargs)
        items = SectionArticleRelation.objects.filter(section__name__iexact="artists").filter(article__status=1).order_by('order')
        featured_artists = Artist.live.filter(featured_artists=True)
        sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="artists").filter(article__status=1).order_by('section__parent__name')
        context['sub_items'] = sub_items
        context['items'] = items
        context['featured_artists'] = featured_artists
        return context

#def index(request):
#    items = SectionArticleRelation.objects.filter(section__name__iexact="artists").filter(article__status=1).order_by('order')
#    artists = Artist.live.all()
#    featured_artists = Artist.live.filter(featured_artists=True)
#    sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="artists").filter(article__status=1).order_by('section__parent__name')
#    return object_list(request, 
#                       queryset=artists, 
#                       template_object_name ='artist',
#                       template_name ='artists/artists_index.html',
#                       extra_context={'items': items, 'sub_items': sub_items, 'featured_artists': featured_artists, })


class ArticleDetailView(DetailView):
    queryset = Article.live.all()
    template_name = 'artists/article_detail.html'
    template_object_name='article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="artists").filter(article__status=1).order_by('section__parent__name')
        artists = Article.live.all()
        context['sub_items'] = sub_items
        context['artists'] = artists
        return context 

#def article_detail(request, slug):
#    articles = Article.live.all()
#    sub_items = SectionArticleRelation.objects.filter(section__parent__name__iexact="artists").filter(article__status=1).order_by('section__parent__name')
#    return object_detail(request, queryset=articles,
#                         slug=slug, slug_field='slug',
#                         template_name = 'artists/article_detail.html',
#                         template_object_name='article',
#                         extra_context={'artists': Artist.live.all,
#                                        'sub_items': sub_items, })

class ArtistDetailView(DetailView):
    queryset = Article.live.all()
    template_name = 'artists/artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        artists = Artist.live.exclude(slug__exact=self.slug)
        context['artists'] = artists
        return context 
                                        
#def artist_detail(request, slug):
#    artist = Artist.live.all()
#    artists = Artist.live.exclude(slug__exact=slug)
#    return object_detail(request, queryset=artist,
#                         slug=slug, slug_field='slug',
#                         template_name = 'artists/artist_detail.html',
#                         extra_context={'artists': artists })

#@login_required
#def artist_info(request):
#    items = SectionArticleRelation.objects.filter(section__name="Participants").filter(article__status=1)
#    return object_list(request, queryset=items,
#                       template_name = 'artists/artists_info.html',
#                       extra_context={'items': items,})

class ArtistInfoView(ListView):
    queryset = SectionArticleRelation.objects.filter(section__name="Participants").filter(article__status=1)
    template_object_name='items'
    template_name = 'artists/artists_info.html'

