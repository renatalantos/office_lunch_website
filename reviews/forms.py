"""
Constructs a product review form
from the model's components for user
"""
from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):
    """
    Extracts fields from review model.
    """

    class Meta:
        """
        Extracts fields from review model
        and styles them.
        """

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
