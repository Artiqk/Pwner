from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article, ArticleCategory


class ArticleListView(TemplateView):
    model = Article
    template_name = 'docs/articles_list.html'