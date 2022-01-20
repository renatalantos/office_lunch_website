from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_number = models.CharField(max_length=4, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    option_grilled = models.BooleanField(default=False, null=True, blank=True)
    lunch_deal = models.BooleanField(default=False, null=True, blank=True)
    calory = models.IntegerField(null=True, blank=True)
    gluten = models.BooleanField(default=False, null=True, blank=True)
    vegan = models.BooleanField(default=False, null=True, blank=True)
    vegetarian = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_rating(self):
        total_stars = sum(int(review['stars']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total_stars / self.reviews.count()
        else:
            return 0
  

    def __str__(self):
        return self.name






   
    
  
