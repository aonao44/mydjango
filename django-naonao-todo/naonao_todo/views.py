from multiprocessing import cpu_count
from django import forms, views
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView)

from naonao_todo.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'naonao_todo/article_list.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('listview:::', context)
        return context


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "naonao_todo/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('detailview:::', context)
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "naonao_todo/article_create_update.html"
    fields = '__all__'
    success_url = reverse_lazy('list')
    print('create::', forms, fields, type(forms))


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "naonao_todo/article_delete.html"
    success_url = reverse_lazy('list')


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "naonao_todo/article_create_update.html"
    fields = '__all__'
    success_url = reverse_lazy('list')
    print('create::', forms, fields, type(forms))
