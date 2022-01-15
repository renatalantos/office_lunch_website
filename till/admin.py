   
from django.contrib import admin
from .models import Order, OrderComponentItem


class OrderComponentItemAdminInline(admin.TabularInline):
    model = OrderComponentItem
    readonly_fields = ('componentitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderComponentItemAdminInline,)

    readonly_fields = ('order_number', 'date_of_order',
                       'delivery_charge', 'order_total',
                       'final_total', 'delivery_date', 
                       'original_basket', 'stripe_pid')

    fields = ('order_number', 'date_of_order', 'full_name','user_profile',
              'email', 'phone_number',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_charge',
              'order_total', 'final_total', 'delivery_date',
              'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date_of_order', 'full_name',
                    'delivery_date', 'order_total', 'delivery_charge',
                    'final_total',)

    ordering = ('-date_of_order',)

admin.site.register(Order, OrderAdmin)
