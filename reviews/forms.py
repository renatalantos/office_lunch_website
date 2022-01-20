from django import forms
from products.models import Product, Category
from .models import ProductReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = '__all__'