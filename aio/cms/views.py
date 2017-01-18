# cms/views.py

from django.views.generic import object_detail
from .models import Article, SectionArticleRelation

def article_detail(request, slug, template, extra)
    articles = Article.live.all()
    return object_detail(request, queryset=articles,
                         slug=slug, slug_field=slug_field,
                         template_name = template,
                         extra_context = extra)
                         
                         
