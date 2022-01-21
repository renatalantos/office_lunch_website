from django.contrib import admin
from .models import ProductReview

# Register your models here.
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (

        'product',
        'user',
        'title',
        'content',
        'rating',
        'date_added',
       
    )
    
admin.site.register(ProductReview, ProductReviewAdmin)