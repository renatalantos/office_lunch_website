"""
Creates order form and its elements.
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Extracts elements to display for user from model.
    """
    class Meta:
        """
        Extracts elements to display for user from model
        and enables styling.
        """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'town_or_city', 'street_address1',
                  'street_address2',
                  'postcode', 'county',
                  'delivery_date',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postcode': 'Postcode',
            'county': 'County',
            'delivery_date': 'Delivery Date',
        }

        self.fields['full_name'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['phone_number'].widget.attrs['required'] = 'required'
        self.fields['town_or_city'].widget.attrs['required'] = 'required'
        self.fields['street_address1'].widget.attrs['required'] = 'required'
        self.fields['postcode'].widget.attrs['required'] = 'required'
        self.fields['county'].widget.attrs['required'] = 'required'
        self.fields['delivery_date'].widget.attrs['class'] = 'form-control datetimepicker-input'
        self.fields['delivery_date'].widget.attrs['required'] = 'required'
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
