
from django.contrib import admin
from django.urls import path
from blogapp.views import PostListView, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='list'),
    path("detail/<int:pk>", PostDetailView.as_view(), name="detail"),

]
