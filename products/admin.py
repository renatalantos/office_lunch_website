"""
Registers product model in admin.
"""
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Lists model components to be displayed in admin.
    """
    list_display = (
        'product_number',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('product_number',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Human friendly category items display.
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
