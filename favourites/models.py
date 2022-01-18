from django.db import models
from django.contrib.auth.models import User

from.products.model import Product

class Favourites:
    """
    Class enables user to have a favourites list
    """
    products = models.ManyToManyField(Product, blank=True)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)