from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import gettext as _
from .forms import ProductReviewForm
from .models import ProductReview
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST)
        if review_form.is_valid():
            try:
                review = review_form.save(commit=False)
                review.reviewer = UserProfile.objects.get(user=request.user)
                review.product = product
                review.save()
                messages.success(request, _('Success! Your review has been added to our website'))
                return redirect(reverse('product_detail', args=[product.id]))
            except ValidationError as e:
                messages.error(request, _('There was an error adding your review to the site. Please check all fields in the form and try again'))
                return redirect(reverse('add_review', args=[product.id]))
    else:
        review_form = ProductReviewForm(initial={
            'reviewer': UserProfile.objects.get(user=request.user)
            })

    template = 'reviews/add_review.html'
    context = {
        'form': review_form,
        'product': product,
    }

    return render(request, template, context=context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(ProductReview, pk=review_id)
    if review.reviewer.user!= request.user:
        messages.error(request, _('You do not have permission to edit this review'))
        return redirect(reverse('product_detail', args=[review.product.id]))

    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, _('Success! The edit you made to your review updated'))
            return redirect(reverse('product_detail', args=[review.product.id]))
    else:
        review_form = ProductReviewForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {
        'form': review_form,
        'review': review,
    }

    return render(request, template, context=context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(ProductReview, pk=review_id)
    if review.reviewer.user!= request.user:
        messages.error(request, _('You do not have permission to delete this review'))
        return redirect(reverse('product_detail', args=[review.product.id]))

    if request.method == 'POST':
        review.delete()
        messages.success(request, _('Review deleted successfully!'))
        return redirect(reverse('product_detail', args=[review.product.id]))
    else:
        template = 'reviews/delete_review.html'
        context = {
            'review': review,
        }

        return render(request, template, context=context)