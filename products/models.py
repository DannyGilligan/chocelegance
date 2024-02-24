from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254) # Required
    friendly_name = models.CharField(max_length=254, null=True, blank=True) # Optional


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) # Optional
    sku = models.CharField(max_length=254, null=True, blank=True) # Optional
    name = models.CharField(max_length=254) # Required
    description = models.TextField() # Required
    price = models.DecimalField(max_digits=6, decimal_places=2) # Required
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) # Optional
    image_url = models.URLField(max_length=1024, null=True, blank=True) # Optional
    image = models.ImageField(null=True, blank=True) # Optional

    def __str__(self):
        return self.name
