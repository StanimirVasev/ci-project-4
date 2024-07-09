from django.shortcuts import render, get_object_or_404
from .models import Post, BlogCategory
from products.models import Category, Subcategory

def blog_list(request):
    posts = Post.objects.all().order_by("-created_on")
    blog_categories = BlogCategory.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {
        'posts': posts,
        'blog_categories': blog_categories,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, "blog/blog.html", context)

def blog_category(request, category_name):
    blog_categories = BlogCategory.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    category = get_object_or_404(BlogCategory, name__iexact=category_name)
    posts = Post.objects.filter(
        blog_categories__name__icontains=category_name
    ).order_by("-created_on")
    context = {
        'category': category,
        'category_name': category_name,
        'posts': posts,
        'blog_categories': blog_categories,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, "blog/blog_category.html", context)

def blog_detail(request, pk):
    blog_categories = BlogCategory.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
        'blog_categories': blog_categories,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, "blog/blog_detail.html", context)
