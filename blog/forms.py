# forms.py
from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'categories')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)