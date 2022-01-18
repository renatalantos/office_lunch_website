from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """A view that renders the shopping basket contents page"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    option_grill = None
    if 'grilled' in request.POST:
        option_grill = request.POST['grilled']
    basket = request.session.get('basket', {})

    if option_grill:
        if item_id in list(basket.keys()):
            if option_grill in basket[item_id]['items_by_option_grill'].keys():
                basket[item_id]['items_by_option_grill'][option_grill] += quantity
                messages.success(request, f'Updated number of {product.name} ({option_grill}) in basket to {basket[item_id]["items_by_option_grill"][option_grill]}')
            else:
                basket[item_id]['items_by_option_grill'][option_grill] = quantity
                messages.success(request, f'Added {product.name} ({option_grill}) to your basket.')
        else:
            basket[item_id] = {'items_by_option_grill': {option_grill: quantity}}
            messages.success(request, f'Added {product.name} ({option_grill}) to your basket.')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated number of {product.name} in basket to {basket[item_id]}.')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket.')
 
    request.session['basket'] = basket
    return redirect(redirect_url)


def change_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    option_grill = None
    if 'grilled' in request.POST:
        option_grill = request.POST['grilled']
    basket = request.session.get('basket', {})

    if option_grill:
        if quantity > 0:
            basket[item_id]['items_by_option_grill'][option_grill] = quantity
            messages.success(request, f'Updated number of {product.name} ({option_grill}) in basket to {basket[item_id]["items_by_option_grill"][option_grill]}')
        else:
            del basket[item_id]['items_by_option_grill'][option_grill]
            if not basket[item_id]['items_by_option_grill']:
                basket.pop(item_id)
                messages.success(request, f'Deleted {product.name} ({option_grill}) from your basket.')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated number of {product.name} in basket to {basket[item_id]}.')
        else:
            basket.pop(item_id)
            messages.success(request, f'Deleted {product.name} from your basket.')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def delete_from_basket(request, item_id):
    """Delete item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        option_grill = None
        if 'grilled' in request.POST:
            option_grill = request.POST['grilled']
        basket = request.session.get('basket', {})

        if option_grill:
            del basket[item_id]['items_by_option_grill'][option_grill]
            if not basket[item_id]['items_by_option_grill']:
                basket.pop(item_id)
            messages.success(request, f'Deleted {product.name} ({option_grill}) from you basket.')    
        else:
            basket.pop(item_id)
            messages.success(request, f'Deleted {product.name} from your basket.')
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error deleting item: {e}')
        return HttpResponse(status=500)

# Create your views here.
