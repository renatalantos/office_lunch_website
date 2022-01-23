from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm 


def contact(request):
    """
    Enables sending user enquiries through
    the contact page.
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():            
            contact_form.save()
            messages.success(request, 'Thank you. Your email has been sent. We will get back to you as soon as possible.')
        else:
            messages.error(request, 'Sorry, your email could not be sent.')
    form = ContactForm()
    return render(request, 'contactus/contact.html')

