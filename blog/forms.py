from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'categories')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)