from django import forms
from .models import Post, BlogCategory
from products.widgets import CustomClearableFileInput

class PostForm(forms.ModelForm):
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
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
