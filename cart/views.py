from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view to render shopping cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Form is submitted to this view. Allows user to add quantity of products to shopping cart """

    quantity = int(request.POST.get('quantity')) # Converts form quantity to integer and sends to server
    redirect_url = request.POST.get('redirect_url') # Where the user will redirected to once the form is submitted
    cart = request.session.get('cart', {}) # Adds 'cart' to session, or creates it if it doesn't, which will allow the user to keep adding items to cart while browsing site, session will persist until user closes browser

    if item_id in list (cart.keys()):
        cart[item_id] += quantity # Increments quantity of specific item in user cart if items_id is already present
    else:
        cart[item_id] = quantity # Adds item_id to cart if it is not already present

    request.session['cart'] = cart # Overwrites the 'cart' variable with the updated value
    return redirect(redirect_url) # Redirects user once process is complete