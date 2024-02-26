from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ This function will be used as a filter to return the subtotal value on the shopping cart page """
    return price * quantity