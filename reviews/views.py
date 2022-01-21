from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import ProductReview
from .forms import ReviewForm
from profiles.models import CustomerProfile

@login_required
def add_review(request, product_id):
    """
    Function enables user to write a review for a product
    and add it to the database.
    """
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        

       
        review_form = ReviewForm(request.POST)
        print(review_form)
        if review_form.is_valid():
            product_review = ProductReview()
            review = review_form.save(commit=False)
            product_review.content = review.content
            product_review.user = CustomerProfile.objects.get(user=request.user)
            product_review.product = product
            product_review.save()        
            messages.success(request, 'Review successful.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Something is wrong with your review form.')
            print('Wrong')
    review_form = ReviewForm()
    template = 'products/product_detail.html'
    context = {
        'review_form': review_form,
        'product':product,
       
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
    if review.user != request.user:
        messages.error(request, 'You are tring to edit a review by someone else.')
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save()
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been updated.')
            return redirect(reverse('products:product_detail', args=[product.id]))
        else:
            messages.warning(request, 'Your review could not be updated.')
     
    else: 
        review_form = ReviewForm(instance=review)
    messages.info(request, 'You are editing your review')
    template = 'products/product_detail.html'
    context = {
        'review_form': review_form,
        'review': review,
        'product': product,
        }
    return render(request, template, context)



@login_required
def delete_review(request, review_id):
    """
    Function enables user to delete a booking after
    it has been made and added to the database.
    """

    review = get_object_or_404(ProductReview, username=request.user.id)
    product = review.product
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review.user != request.user:
            messages.error(request, 'You are tring to delete a review by someone else.')
        if review.delete():
            messages.success(request, 'Your review has been deleted.')
        return redirect(reverse('products:product_detail', args=[product.id]))
    
    review_form = ReviewForm(instance=review)
    template = 'products/product_detail.html'
   
    context = {
        'review_form': review_form,
        'review': review,
        'product': product,
    }
    return render(request, template, context)
