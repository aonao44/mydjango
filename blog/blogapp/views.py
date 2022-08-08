from django.http import Http404

from gc import get_objects
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blogapp.models import Post


class PostListView(ListView):
    model = Post
    template_name = "html/post_list.html"
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = "html/post_detail.html"

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        print(self.request.user.is_superuser)
        print(post.is_published)

        if post.is_published or self.request.user.is_superuser:
            return post
        else:
            raise Http404
