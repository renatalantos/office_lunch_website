from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })


        else:
            product = get_object_or_404(Product, pk=item_id)
            for option_grill, quantity in item_data['items_by_option_grill'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'option_grill': option_grill,
                })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    final_total = delivery + total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'final_total': final_total,
    }

    return context