from django import forms
from products.models import Product, Category
from .models import ProductReview

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = ProductReview
        exclude = ('product', 'user', 'date_added')

    def __init__(self, *args, **kwargs):
        """   
        Remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        

        
        self.fields['content'].label = False
        self.fields['title'].label = False
        self.fields['rating'].label = False


  