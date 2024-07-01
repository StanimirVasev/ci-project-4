from django.shortcuts import render
from products.models import Category, Subcategory

def index(request):
    """ A view to return the index page """
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    context = {
        'categories': categories,
        'subcategories': subcategories,
    }

    return render(request, 'home/index.html', context)