from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_number',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('product_number',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'date_added',
       
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)