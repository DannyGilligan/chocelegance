from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254) # Required
    friendly_name = models.CharField(max_length=254, null=True, blank=True) # Optional


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



