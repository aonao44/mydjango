# config
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('naonao_todo.urls')),
    path('accounts/', include('accounts.urls')),
]
