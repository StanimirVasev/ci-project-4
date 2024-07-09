from django import forms
from .models import Post, BlogCategory

class PostForm(forms.ModelForm):
    # Define the blog_categories field as a ModelChoiceField
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
