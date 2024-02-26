from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_cart(request):
    """ A view to render shopping cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Form is submitted to this view. Allows user to add quantity of products to shopping cart """

    quantity = int(request.POST.get('quantity')) # Converts form quantity to integer and sends to server
    redirect_url = request.POST.get('redirect_url') # Where the user will redirected to once the form is submitted
    
    size = None # Product size is initialised with a None value
    if 'product_size' in request.POST: # If Product size is included in the POST request, the size variable will be updated to that value
        size = request.POST['product_size']
    
    cart = request.session.get('cart', {}) # Adds 'cart' to session, or creates it if it doesn't, which will allow the user to keep adding items to cart while browsing site, session will persist until user closes browser
  
    if size:
        if item_id in list(cart.keys()): # If item is in the cart, checks if item of same size exists and updates quantity
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else: # If item not in cart, it will be added as a dictionary
            cart[item_id] = {'items_by_size': {size: quantity}}
    else: # If there is no size for the product, this block of code will run
        if item_id in list (cart.keys()):
            cart[item_id] += quantity # Increments quantity of specific item in user cart if items_id is already present
        else:
            cart[item_id] = quantity # Adds item_id to cart if it is not already present

    request.session['cart'] = cart # Creates session variable and overwrites the 'cart' variable with the updated value
    return redirect(redirect_url) # Redirects user once process is complete





def adjust_cart(request, item_id):
    """ This view will adjust the quantity of the products in the cart and the related amount when the update button is clicked """

    quantity = int(request.POST.get('quantity')) # Converts form quantity to integer and sends to server
    size = None # Product size is initialised with a None value
    if 'product_size' in request.POST: # If Product size is included in the POST request, the size variable will be updated to that value
        size = request.POST['product_size']
    
    cart = request.session.get('cart', {}) # Adds 'cart' to session, or creates it if it doesn't, which will allow the user to keep adding items to cart while browsing site, session will persist until user closes browser
  
    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id) 

    else: # If there is no size for the product, this block of code will run
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop[item_id]

    request.session['cart'] = cart # Creates session variable and overwrites the 'cart' variable with the updated value
    return redirect(reverse(view_cart)) # Redirects user back to same page once process is complete



def remove_from_cart(request, item_id):
    """ This view will remove the item from the cart when the remove button is clicked """

    try:
        size = None # Product size is initialised with a None value
        if 'product_size' in request.POST: # If Product size is included in the POST request, the size variable will be updated to that value
            size = request.POST['product_size']
        
        cart = request.session.get('cart', {}) # Adds 'cart' to session, or creates it if it doesn't, which will allow the user to keep adding items to cart while browsing site, session will persist until user closes browser
    
        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop[item_id] 


        else: # If there is no size for the product, this block of code will run
            cart.pop(item_id)

        request.session['cart'] = cart # Creates session variable and overwrites the 'cart' variable with the updated value
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)