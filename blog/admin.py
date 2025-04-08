from django.contrib import admin

from .models import BlogDetails


@admin.register(BlogDetails)
class BlogDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_active',
        'blog_title',
        'blog_image',
        'blog_content',
    )
    list_filter = ('is_active',)
    list_editable=('is_active',)