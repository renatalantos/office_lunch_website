from django.contrib import admin
from .models import ProductReview

# Register your models here.
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'date_added',
        'content',
        'stars',
       
    )
admin.site.register(ProductReview, ProductReviewAdmin)