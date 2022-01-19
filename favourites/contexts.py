from dajngo.http import Http404
from django.shortcuts import get_object_or_404

from.models import Favourites


def favourites_contents(request):
    """
    Context for favourites to display favourites count
    """
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
        favourites_items = favourites.products.all()
        favourites_count = len(favourites_items)
    except Http404:
        favourites_count = None

    context = {
        'favourites_count': favourites_count,
    }
    return context