"""
Registers review model in the admin.
"""
from django.contrib import admin
from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    """
    Lists model components in admin.
    """
    list_display = (

        'product',
        'user',
        'title',
        'content',
        'rating',
        'date_added',

    )


admin.site.register(ProductReview, ProductReviewAdmin)
