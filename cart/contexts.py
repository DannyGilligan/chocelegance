# Handles the cart_items variable

from decimal import Decimal
from django.conf import settings
from django.shotcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    This is a contexts processor to make the 'context' dictionary below available across the entire application
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items(): # Cart variable relates to the session
        product = get_object_or_404(Product, pk=item_id) # Gets product
        total += quantity * product.price # Adds quantity multiplied by price to total
        product_count += quantity # Increments the quantity
        bag_items.append({ # Dictionary is added to list of cart items containing details stored in the Product object
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = { 'cart_items': cart_items,
                'total': total,
                'product_count': product_count,
                'delivery': delivery,
                'free_delivery_delta': free_delivery_delta,
                'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
                'grand_total': grand_total,
    }

    return context