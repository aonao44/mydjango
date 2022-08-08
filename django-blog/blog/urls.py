

from django.urls import path

from blog.views import (
    Postlistview,
    Postdetailview,
    CategoryPostlistView,
    TagPostlistview,
    SearchPostlistview
)

# app_name = 'blog'

urlpatterns = [
    path('', Postlistview.as_view(), name='post-lists'),
    path('post/<int:pk>/', Postdetailview.as_view(), name='post-detail'),
    path('category/<str:slug>/', CategoryPostlistView.as_view(), name='category-post-list'),
    path('tag/<str:slug>/', TagPostlistview.as_view(), name='tag-post-list'),
    path('search/', SearchPostlistview.as_view(), name='search-post-list'),
]
