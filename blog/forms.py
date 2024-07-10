from django import forms
from .models import Post, BlogCategory

class PostForm(forms.ModelForm):
    blog_categories = forms.ModelChoiceField(
        queryset=BlogCategory.objects.all(),
        widget=forms.Select,
    )

    class Meta:
        model = Post
        fields = ('title', 'body', 'blog_categories', 'image_url', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use friendly names in the form fields for blog_categories
        self.fields['blog_categories'].widget.choices = [
            (cat.id, cat.get_friendly_name()) for cat in BlogCategory.objects.all()
        ]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'friendly_title', 'blog_categories', 'body', 'image']
        labels = {
            'title': 'Blog Title',
            'friendly_title': 'Friendly Title',
            'blog_categories': 'Blog Category',
            'body': 'Content',
            'image': 'Blog Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'friendly_title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_categories': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blog_categories'].queryset = BlogCategory.objects.all()
        self.fields['blog_categories'].label_from_instance = lambda obj: obj.get_friendly_name()