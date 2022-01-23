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
    content = review.content
    rating = review.rating
    date_added = review.date_added
    title = review.title
   
    current_user = CustomerProfile.objects.get(user=request.user)
    if request.user.is_superuser:
        messages.info(request, 'You are editing reviews as a superuser.')
    elif review.user != current_user:
        messages.error(request, 'You are tring to edit a review by someone else.')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        messages.info(request, 'You are editing your review')
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)

        if review_form.is_valid(): 
            review = review_form.save(commit=False)       
            review.user = CustomerProfile.objects.get(user=request.user)    
            # review.content = content
            # review.rating = rating
            # review.title = title
            # review.date_added = date_added
            # review.product = product
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
        return redirect(reverse('product_detail', args=[product.id]))
    
    review_form = ReviewForm(instance=review)
    template = 'products/product_detail.html'
   
    context = {
        'review_form': review_form,
        'review': review,
       
    }
    return render(request, template, context)


# @login_required
# def add_review(request, product_id):
#     """
#     A view to add a review to a product
#     """
#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         review_form = ReviewForm(request.POST)

#         if review_form.is_valid():
#             already_reviewed = ProductReview.objects.filter(product=product,
#                                                      user=request.user)
#             if not already_reviewed:
#                 ProductReview.objects.create(
#                         product=product,
#                         user=request.user,
#                         product_rating=request.POST['product_rating'],
#                         review_text=request.POST['review_text'],
#                 )
#                 messages.info(request, 'Successfully added a review!')
#             else:
#                 messages.error(request, 'You have already reviewed '
#                                         'this product!')
#             return redirect(reverse('product_detail', args=[product.id]))

#         messages.error(request, 'Failed to add product review')
#     messages.error(request, 'Invalid Method.')
#     return redirect(reverse('product_detail', args=[product.id]))

# @login_required
# def edit_review(request, review_id):
#     """
#     Edit exisiting review
#     """
#     review = get_object_or_404(Review, pk=review_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, instance=review)

#         if form.is_valid():
#             # review_form.save()
#             messages.info(request, 'Successfully updated your review!')
#             return redirect(reverse('product_detail', args=[review.id]))
#         else:
#             messages.error(request, 'Failed to update product review')
#     else:
#         form = ReviewForm(instance=review)
#         messages.info(request, 'You are editing your review for ' +
#                       f'{review.product.name}')

#     template = 'products/edit_review.html'
#     context = {
#         'form': form,
#         'review': review,
#     }

#     return render(request, template, context)