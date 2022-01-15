
from django import forms
from .models import CustomerProfile


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """   
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_email': 'Email',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_postcode': 'Postcode',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['required'] = 'required'
        self.fields['default_email'].widget.attrs['required'] = 'required'
        self.fields['default_town_or_city'].widget.attrs['required'] = 'required'
        self.fields['default_street_address1'].widget.attrs['required'] = 'required'
        self.fields['default_postcode'].widget.attrs['required'] = 'required'
        self.fields['default_county'].widget.attrs['required'] = 'required'    
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

  