from django.shortcuts import render, get_object_or_404
from .models import CustomerProfile
from .forms import CustomerProfileForm
from django.contrib import messages

from till.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(CustomerProfile, user=request.user)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = CustomerProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'till/till_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)