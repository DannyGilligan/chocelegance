from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False) # Order no. is unique and permanent
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True) # Optional
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True) # Optional
    date = models.DateTimeField(auto_now_add=True) # Automatically sets order date and time when order is created
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0) # Calculated when order is saved
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0) # Calculated when order is saved
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0) # Calculated when order is saved

