from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.prefetch_related('scopes')
    context = {'object_list':articles}
    ordering = '-published_at'

    return render(request, template, context)
