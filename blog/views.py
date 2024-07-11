from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from .models import Post, BlogCategory
from products.models import Category, Subcategory
from .forms import BlogForm


def blog_list(request, page=1):
    posts = Post.objects.all().order_by("-created_on")
    blog_categories = BlogCategory.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    paginator = Paginator(posts, 12)

    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'blog_categories': blog_categories,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, "blog/blog.html", context)


def blog_category(request, category_name, page=1):
    blog_categories = BlogCategory.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    category = get_object_or_404(BlogCategory, name__iexact=category_name)

    posts = Post.objects.filter(
        blog_categories=category
        ).order_by("-created_on")

    paginator = Paginator(posts, 12)

    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'category_name': category_name,
        'page_obj': page_obj,
        'posts': page_obj.object_list,
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


@login_required
def add_blog(request):
    """ Add a blog post """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only superusers can add blog posts.'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Successfully added the blog post!'
                )
            return redirect(reverse('blog_list'))
        else:
            messages.error(
                request,
                'Failed to add the blog post. Please ensure the form is valid.'
                )
    else:
        form = BlogForm()

    return render(
        request,
        'blog/add_blog.html',
        {'form': form}
    )


@login_required
def edit_blog(request, pk):
    """ Edit a blog post """
    post = get_object_or_404(Post, pk=pk)

    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only superusers can edit blog posts.'
            )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Successfully updated the blog post!'
            )
            return redirect(reverse('blog_detail', args=[post.pk]))
        else:
            messages.error(
                request,
                'Failed to update the blog post. '
                'Please ensure the form is valid.'
            )
    else:
        form = BlogForm(instance=post)
        messages.info(
            request,
            f'You are editing {post.title}'
        )

    return render(
        request,
        'blog/edit_blog.html',
        {'form': form, 'post': post}
    )


@login_required
def delete_blog(request, pk):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('blog_list'))
