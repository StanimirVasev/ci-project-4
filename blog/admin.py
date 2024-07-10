from django.contrib import admin
from .models import BlogCategory, Post
from .forms import PostForm

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('friendly_name',)
    search_fields = ('name', 'friendly_name')

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = (
        'title',
        'friendly_title',
        'display_blog_categories',
        'created_on',
    )
    list_filter = ('created_on', 'blog_categories')
    ordering = ('-created_on',)
    search_fields = ('title', 'body')

    def display_blog_categories(self, obj):
        return obj.blog_categories.get_friendly_name() if obj.blog_categories else 'None'
    display_blog_categories.short_description = 'Blog Category'

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Post, PostAdmin)
