from django.contrib import admin
from blog.models import BlogCategory, Post

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )
    ordering = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'friendly_title',
        'created_on',
    )
    list_filter = ('created_on',)
    ordering = ('created_on',)

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Post, PostAdmin)
