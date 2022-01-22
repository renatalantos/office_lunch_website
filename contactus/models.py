from django.db import models

class ContactUs(models.Model):
    """
    Enables user to send emails to company
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    enquiry = models.TextField()

    def __str__(self):
        return str(self.name)

