from django.contrib import admin
from blog.models import BlogCategory, Post
from blog.forms import PostForm, BlogCategoryForm

class BlogCategoryAdmin(admin.ModelAdmin):
    form = BlogCategoryForm
    list_display = (
        'name',
        'friendly_name',
    )
    ordering = ('name',)
    search_fields = ('name', 'friendly_name') 

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = (
        'title',
        'friendly_title',
        'created_on',
    )
    list_filter = ('created_on', 'blog_categories') 
    ordering = ('-created_on',)  
    search_fields = ('title', 'body')  

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Post, PostAdmin)
