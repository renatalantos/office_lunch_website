"""
Views to enable viewing favourite items,
adding items to favourites,
and deleting from favourites.
"""
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Favourites


@login_required
def view_favourite_list(request):
    """A view that renders the favourites page"""
    favourites_count = 0
    try:
        all_favourites = Favourites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favourites_items = None
    else:
        favourites_items = all_favourites.products.all()
        favourites_count = all_favourites.products.all().count()

    template = 'favourites/favourite_list.html'
    context = {
        'favourites_items': favourites_items,
        'favourites_count': favourites_count,
    }
    return render(request, template, context)


@login_required
def add_product_to_favourites(request, item_id):
    """Add a particular product to favourites"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        favourites = Favourites.objects.create(username=request.user)
    if product in favourites.products.all():
        messages.info(request, 'This item has already been added to your favourites.')
    else:
        favourites.products.add(product)
        messages.success(request, 'The item has been added to favourites.')
    return redirect(reverse('product_detail', args=[item_id]))
 

@login_required
def remove_product_from_favourites(request, item_id, redirect_from):
    """Add a particular product to favourites"""
    product = get_object_or_404(Product, pk=item_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)
    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.info(request, 'This item has been removed from your favourites.')
    else:
        messages.error(request, 'This product is not in your favourites.')
    if redirect_from == 'favourites':
        redirect_url = reverse('favourites')
    else:
        redirect_url = reverse('product_detail', args=[item_id])
    return redirect(redirect_url)