from django.shortcuts import render
from products.models import Category, Subcategory

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    context = {
        'categories': categories,
        'subcategories': subcategories,
    }

    return render(request, 'bag/bag.html', context)