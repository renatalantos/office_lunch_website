"""
Form to enable product owner to upload products.
"""

from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Class to describe product components.
    """

    class Meta:
        """
        Class to collect fields from model.
        """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-1'
