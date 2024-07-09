from django.contrib import admin
from blog.models import BlogCategory, Post
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
        'created_on',
        'display_blog_categories',
    )
    list_filter = ('created_on', 'blog_categories')
    ordering = ('-created_on',)
    search_fields = ('title', 'body')

    def display_blog_categories(self, obj):
        return ', '.join([category.get_friendly_name() for category in obj.blog_categories.all()])
    display_blog_categories.short_description = 'Blog Categories'

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Post, PostAdmin)
