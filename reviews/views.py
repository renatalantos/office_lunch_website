from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import ProductReview
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """
    Function enables user to write a review for a product
    and add it to the database.
    """
    review_form = ReviewForm(request.POST)
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        if review_form.is_valid():
            review = review_form.save()
            review.user = request.user
            review.product = request.product
            review.save()
            messages.success(request, 'Review successful.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Something is wrong with you reviews.')
    review_form = ReviewForm()
    template = 'products/product_detail.html'
    context = {
        'review_form': review_form,
    
        }
   
    return render(request, template, context)



@login_required
def edit_review(request, review_id):
    """
    Function enables user to edit a booking after
    it has been made and added to the database.
    """
   
    existing_review = get_object_or_404(ProductReview, pk=review_id)
    product = existing_review.product
    if existing_review.user != request.user:
        messages.error(request, 'You are tring to edit a review by someone else.')
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=existing_review)
        if review_form.is_valid():
            existing_review = review_form.save()
            existing_review.user = request.user
            existing_review.save()
            messages.success(request, 'Your review has been updated.')
            return redirect(reverse('products:product_detail', args=[product.id]))
        else:
            messages.warning(request, 'Your review could not be updated.')
     
    else: 
        review_form = ReviewForm(instance=existing_review)
    messages.info(request, 'You are editing your review')
    template = 'products/product_detail.html'
    context = {
        'review_form': review_form,
        'existing_review': existing_review,
        'product': product,
        }
    return render(request, template, context)



@login_required
def delete_review(request, review_id):
    """
    Function enables user to delete a booking after
    it has been made and added to the database.
    """

    existing_review = get_object_or_404(ProductReview, username=request.user.id)
    product = existing_review.product
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=existing_review)
        if existing_review.user != request.user:
            messages.error(request, 'You are tring to delete a review by someone else.')
        if existing_review.delete():
            messages.success(request, 'Your review has been deleted.')
        return redirect(reverse('products:product_detail', args=[product.id]))
    
    

    review_form = ReviewForm(instance=existing_review)
    template = 'products/product_detail.html'
   
    context = {
        'review_form': review_form,
        'existing_review': existing_review,
        'product': product,
    }
    return render(request, template, context)
