from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from .forms import ProductReviewForm
from .models import ProductReview


@login_required
def add_review(request):
    '''
    View that returns the add a review view
    '''
    review_form = ProductReviewForm()

    # If user is authenticated then review form will show
    if request.user.is_authenticated:
        review_form = ProductReviewForm(initial={
            'reviewer': UserProfile.objects.get(user=request.user)
            })
    else:
        # If user is unregistered then they form will not show
        review_form = ProductReviewForm()

    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST)
        sender = UserProfile.objects.get(user=request.user)

        if review_form.is_valid():
            try:
                review_form.save()
                messages.success(request, "Success! Your review has been \
                                           added to our website")
                return redirect(reverse('home'))
            except Exception as e:
                messages.error(request, "There was an error adding your \
                                         review to the site. Please check all \
                                         fields in the form and try again")
                return redirect(reverse('add_review'))
        else:
            pass

    template = 'reviews/add_review.html'
    context = {
        'form': review_form,
    }

    return render(request, template, context=context)
