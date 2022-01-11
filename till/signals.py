from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderComponentItem

@receiver(post_save, sender=OrderComponentItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update total when a new order is created
    """
    instance.order.update_total()

@receiver(delete_save, sender=OrderComponentItem)
def delete_on_save(sender, instance, **kwargs):
    """
    Update total on componentitem delete
    """
    instance.order.update_total()