from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart yet")
        return redirect(reverse('products'))


    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OpLjeEr1kmktexZBqeyQg88vR8Q1U8vOI6ZsClidtrgQkz6yQZKkFy0ofL0RaI6LJYZHnK9WhkoHuM3Q2pm6bLq009uIIwlUi',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
