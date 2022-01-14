import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime
from products.models import Product




class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20,
                                null=True,
                                blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date_of_order = models.DateTimeField(auto_now_add=True)
    cutoff = datetime.time(15, 59)  
    
    def validate_delivery_date(delivery_date):
        """
        Function to validate date so that
        booking date is not in the past.
        """
        if delivery_date < timezone.now():
            raise ValidationError("Delivery date cannot be in the past")
    delivery_date = models.DateTimeField(
                            null=True,
                            blank=True,
                            validators=[validate_delivery_date])

    # def validate_delivery_date(delivery_date):
    #         """
    #         Function to validate date so that
    #         booking date is not in the past.
    #         """
    #         date_of_order = models.DateTimeField(auto_now_add=True)
    #         if delivery_date < timezone.now():
    #             raise ValidationError("Delivery date cannot be in the past")
    #         cutoff = date.time(15, 59)
    #         if date_of_order > date_of_order.cutoff and delivery_date == datetime.date.today():
    #             raise ValidationError("Order placed too late\
    #                                 for today's delivery")

    # delivery_date = models.DateTimeField(
    #                             null=True,
    #                             blank=True,
    #                             validators=[validate_delivery_date])




    delivery_charge = models.DecimalField(max_digits=6,
                                          decimal_places=2,
                                          null=False,
                                          default=0)
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    final_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _create_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.componentitems.aggregate(Sum('componentitem_total'))['componentitem_total__sum'] or 0
     
        self.delivery_charge = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
       
        self.final_total = self.order_total + self.delivery_charge
        self.save()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderComponentItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='componentitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    grilled = models.CharField(max_length=11, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    componentitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the componentitem total
        and update the order total.
        """
        self.componentitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product nr {self.product.product_number} on order {self.order.order_number}'
