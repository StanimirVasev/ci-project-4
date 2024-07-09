from django.contrib import admin
from blog.models import BlogCategory, Post

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('friendly_name',)
    search_fields = ('name', 'friendly_name')

class PostAdmin(admin.ModelAdmin):
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
        """Format blog categories for display in list view."""
        return ', '.join(category.name for category in obj.blog_categories.all())
    display_blog_categories.short_description = 'Blog Categories'

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Post, PostAdmin)
