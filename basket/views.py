from django.shortcuts import render, redirect


def view_basket(request):
    """A view that renders the shopping basket contents page"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

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
            else:
                basket[item_id]['items_by_option_grill'][option_grill] = quantity
        else:
            basket[item_id] = {'items_by_option_grill': {option_grill: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity
 
    request.session['basket'] = basket
    return redirect(redirect_url)