from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def till(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'till/till.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JwUnEHVnsqPPeyfsZsxNI78kCws8KTpFwP91tGn2fsSSrUoO221NDev3BoSnA6tlaedvhGRsEN0RKR5OExOyJBt00gXKtTM1p',
        'client_secret': 'test client_secret',
    }

    return render(request, template, context)
