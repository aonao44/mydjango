from pprint import pprint
from blog.models import Post, Category, Tag
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django import http
from unicodedata import category
from operator import concat
from multiprocessing import context
import django


from django.db.models import Q


class Postlistview(ListView):
    model = Post
    template_name = 'blog/post_lists.html'
    context_object_name = "models"

    def get_queryset(self):
        posts = super().get_queryset()
        print('query_nao:', posts, type(posts))

        return posts.order_by('-updated_at', '-created_at')


class Postdetailview(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        print('object1_nao:', post, type(post))
        if post.is_published or self.request.user.is_authenticated:
            print('object2_nao:', post, type(post))
            return post
        else:
            raise Http404


class CategoryPostlistView(ListView):
    model = Post
    template_name = 'blog/post_lists.html'
    context_object_name = "models"

    def get_queryset(self):
        slug = self.kwargs['slug']
        print('='*30)
        print('self___', vars(self))
        print('self_kwargs____', self.kwargs)
        print('='*30)
        self.category = get_object_or_404(Category, slug=slug)

        return super().get_queryset().filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category'] = self.category
        # pprint(context)

        return context


class TagPostlistview(ListView):
    model = Post
    template_name = 'blog/post_lists.html'
    context_object_name = "models"

    def get_queryset(self):
        slug = self.kwargs['slug']
        self.tag = get_object_or_404(Tag, slug=slug)
        return super().get_queryset().filter(tag=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tag'] = self.tag

        return context


class SearchPostlistview(ListView):
    model = Post
    template_name = 'blog/post_lists.html'
    context_object_name = "models"

    def get_queryset(self):
        self.query = self.request.GET.get('query') or ""
        queryset = super().get_queryset()

        if self.query:
            queryset = queryset.filter(
                Q(title__icontains=self.query) | Q(content__icontains=self.query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['query'] = self.query

        return context
