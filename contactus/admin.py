"""
Register ContactUs model
in admin.
"""

from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    """
    Class to display ContactUs model in admin.
    """
    list_display = ('name', 'email', 'enquiry',)


admin.site.register(ContactUs, ContactUsAdmin)
