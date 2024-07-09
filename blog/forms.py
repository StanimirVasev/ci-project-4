from django import forms
from .models import Post, BlogCategory

class PostForm(forms.ModelForm):
    blog_categories = forms.ModelMultipleChoiceField(
        queryset=BlogCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ('title', 'body', 'blog_categories', 'image_url', 'image')


class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ('name', 'friendly_name')
