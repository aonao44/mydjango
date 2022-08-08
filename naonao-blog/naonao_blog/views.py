from xml.etree.ElementTree import Comment
from django.db.models import Q
from pprint import pprint
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from naonao_blog.models import Post, Category, Tag, Comment, Reply
from naonao_blog.forms import CommentForm, ReplyForm


class PostListView(ListView):
    model = Post
    template_name = "naonaoblog/post_list.html"
    context_object_name = 'posts'
    paginate_by = 3

    # def get_queryset(self):
    #     posts = super().get_queryset()
    #     print('queryset:', posts)

    #     return posts.order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = "naonaoblog/post_detail.html"

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.is_published or self.request.user.is_authenticated:
            return post
        else:
            raise Http404


class CategoryPostListView(ListView):
    model = Post
    template_name = "naonaoblog/post_list.html"
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        url = self.kwargs['slug']
        self.category = get_object_or_404(Category, slug=url)

        return super().get_queryset().filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category

        return context


class TagPostListView(ListView):
    model = Post
    template_name = "naonaoblog/post_list.html"
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        url = self.kwargs['slug']
        self.tag = get_object_or_404(Tag, slug=url)
        return super().get_queryset().filter(tag=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag

        return context


class SearchPostListView(ListView):
    model = Post
    template_name = "naonaoblog/post_list.html"
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        self.query = self.request.GET.get('query') or ""
        queryset = super().get_queryset()

        if self.query:
            queryset = queryset.filter(
                Q(title__icontains=self.query) | Q(content__icontains=self.query)
            )

        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_published=True)

        self.post_count = len(queryset)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        context['post_count'] = self.post_count

        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)

        post_pk = self.kwargs['post_pk']
        post = get_object_or_404(Post, pk=post_pk)

        comment.post = post
        comment.save()

        return redirect('post-detail', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_pk = self.kwargs['post_pk']
        context['post'] = get_object_or_404(Post, pk=post_pk)
        return context


class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyForm

    def form_valid(self, form):
        comment = form.save(commit=False)

        comment_pk = self.kwargs['comment_pk']
        comment = get_object_or_404(Post, pk=comment_pk)

        comment.post = comment
        comment.save()

        return redirect('post-detail', pk=comment.post.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_pk = self.kwargs['comment_pk']
        context['comment'] = get_object_or_404(Post, pk=comment_pk)
        return context
