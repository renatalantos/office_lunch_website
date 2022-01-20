from django.db import models
from django.contrib.auth.models import User


class ProductReview(models.Model):
    product = models.ForeignKey('products.Product', null=True, blank=True, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviewer', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

