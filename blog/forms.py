from django import forms
from .models import Post, BlogCategory
from .widgets import CustomClearableFileInput

class PostForm(forms.ModelForm):
    # Use CustomClearableFileInput for the image field
    image = forms.ImageField(
        widget=CustomClearableFileInput
    )
    
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
