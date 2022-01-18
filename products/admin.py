from django.contrib import admin
from .models import Product, Category

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

class FavouriteAdmin(admin.ModelAdmin):
    list_display = (
        'is_fav',
       
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
