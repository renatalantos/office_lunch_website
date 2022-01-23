from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from profiles.models import CustomerProfile

class ProductReview(models.Model):
    """
    Product Review Model
    """
    class Meta:
        ordering = ['-date_added']

    rating_selection = (
        (5, '5 stars'),
        (4, '4 stars'),
        (3, '3 stars'),
        (2, '2 stars'),
        (1, '1 stars'),
    )

    product = models.ForeignKey(Product,
                                related_name='reviews',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
    user = models.ForeignKey(CustomerProfile,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=254, null=True, blank=True)
    content = models.TextField(default='', null=True, blank=True)
    rating = models.IntegerField(choices=rating_selection, default=3, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

