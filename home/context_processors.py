from blog.models import BlogCategory
from products.models import Category, Subcategory


def blog_and_product_categories_processor(request):
    """
    A context processor to provide blog categories and product categories
    to all templates.
    """
    blog_categories = BlogCategory.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return {
        'blog_categories': blog_categories,
        'categories': categories,
        'subcategories': subcategories,
    }
