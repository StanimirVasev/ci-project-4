from django import forms
from .models import Post, BlogCategory

class PostForm(forms.ModelForm):
    categories = forms.ModelChoiceField(
        queryset=BlogCategory.objects.all(),
        widget=forms.Select, 
    )

    class Meta:
        model = Post
        fields = ('title', 'body', 'categories', 'image_url', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use friendly names in the form fields
        self.fields['categories'].widget.choices = [
            (cat.id, cat.get_friendly_name()) for cat in BlogCategory.objects.all()
        ]
