from django.contrib import admin
from blog.models import Category, Comment, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'last_modified')
    list_filter = ('created_on', 'last_modified')
    search_fields = ('title', 'body')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_on', 'post')
    list_filter = ('created_on',)
    search_fields = ('author', 'body')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)