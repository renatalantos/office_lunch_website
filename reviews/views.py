"""
Views to set up logic for user
to add, edit and delete reviews.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from profiles.models import CustomerProfile
from .models import ProductReview
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """
    Function enables user to write a review for a product
    and add it to the database.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            product_review = ProductReview()
            review = review_form.save(commit=False)
            product_review.user = review.user
            product_review.date_added = review.date_added
            product_review.content = review.content
            product_review.rating = review.rating
            product_review.title = review.title
            product_review.user = CustomerProfile.objects.get(user=request.user)
            product_review.product = product
            product_review.save()
            messages.success(request, 'Review successful.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Something is wrong with your review form.')

    review_form = ReviewForm()
    template = 'products/product_detail.html'
    context = {
        'review_form': review_form,
        'product': product,
        'edit': True,
    }
    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """
    Function enables user to edit a booking after
    it has been made and added to the database.
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    current_user = CustomerProfile.objects.get(user=request.user)
    if review.user != current_user:
        messages.error(request, 'You are tring to edit a review by someone else.')
        return redirect(reverse('product_detail', args=[product.id]))
    if review.user == current_user or request.user.is_superuser:

        if request.method == "POST":
            review_form = ReviewForm(request.POST, instance=review)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = CustomerProfile.objects.get(user=request.user)
                product = review.product
                review.save()
                messages.success(request, 'Your review has been updated.')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.warning(request, 'Your review could not be updated.')
        else:
            review_form = ReviewForm(instance=review)
    template = 'products/product_detail.html'
    context = {
        'review_form': review_form,
        'review': review,
        'product': product,
        'edit': True,
        }
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    View enables user to delete their own reviews
    and superuser to delete reviews by others besides.
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    current_user = CustomerProfile.objects.get(user=request.user)
    if review.user != current_user and not request.user.is_superuser:
        messages.error(request, 'You are tring to delete a review by someone else.')
        return redirect(reverse('product_detail', args=[product.id]))
    if review.user == current_user or request.user.is_superuser:
        review.delete()
        messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
