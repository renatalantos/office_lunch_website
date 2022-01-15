from django.shortcuts import render, get_object_or_404
from .models import CustomerProfile
from .forms import CustomerProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(CustomerProfile, user=request.user)
    orders = profile.orders.all()

    form = CustomerProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)