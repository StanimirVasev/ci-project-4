from django.shortcuts import render, get_object_or_404
from .models import Post, BlogCategory
from products.models import Category, Subcategory
from .forms import BlogForm 

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
    
    # Correctly fetch the category object
    category = get_object_or_404(BlogCategory, name__iexact=category_name)
    
    # Filter posts based on the `blog_categories` field
    posts = Post.objects.filter(blog_categories=category).order_by("-created_on")
    
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
    
    # Fetch the specific post
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post': post,
        'blog_categories': blog_categories,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, "blog/blog_detail.html", context)


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {'form': form})