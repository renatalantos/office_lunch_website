"""
Displays contact form for user.
"""
from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    """
    Contact form to be displayed on Contact Us page
    """

    class Meta:
        """
        Extracts fields from model.
        """
        model = ContactUs
        fields = '__all__'
