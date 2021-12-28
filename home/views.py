from django.shortcuts import render


def index(request):
    """
    A view that returns the index page.
    """
    return render(request, 'home/index.html')


def search(request):
    """
    A view that returns the search page.
    """
    return render(request, 'home/search.html')