from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Category, Subcategory

from .forms import OrderForm


def checkout(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'categories': categories,
        'subcategories': subcategories,
    }

    return render(request, template, context)