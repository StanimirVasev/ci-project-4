from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Subcategory

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    query = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    category = None
    subcategory = None
    sort = None
    direction = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'name'
            if sortkey == 'category':
                sortkey = 'category__name'
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_name = request.GET['category']
            category = get_object_or_404(Category, name=category_name)
            if 'subcategory' in request.GET:
                subcategory_name = request.GET['subcategory']
                subcategory = get_object_or_404(Subcategory, name=subcategory_name, category=category)
                products = products.filter(subcategory=subcategory)
            else:
                products = products.filter(category=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
        'subcategories': subcategories,
        'category': category,
        'subcategory': subcategory,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    context = {
        'product': product,
        'categories': categories,
        'subcategories': subcategories,
    }

    return render(request, 'products/product_detail.html', context)