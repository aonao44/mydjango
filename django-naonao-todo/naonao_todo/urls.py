
# naonao_todo

from django.contrib import admin
from django.urls import path

from naonao_todo.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleUpdateView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('create', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
]
