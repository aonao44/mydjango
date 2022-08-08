from django.contrib import admin
from naonao_blog.models import Post, Category, Tag, Comment, Reply

# Register your models here.


class PostAdimin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created_at',
        'updated_at',
        'is_published')
    search_fields = ('title', 'content')
    list_filter = ('category', )


admin.site.register(Post, PostAdimin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
