from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article, ArticleCategory


class BaseView(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['active_page'] = 'docs'
        
        return context
    


class ArticleListView(BaseView):
    model = Article
    
    template_name = 'docs/articles_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    