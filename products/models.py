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
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    RATING_CHOICES = (
            (5, '5'),
            (4, '4'),
            (3, '3'),
            (2, '2'),
            (1, '1'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
   

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add='true')
    comment = models.TextField()
    

    def __str__(self):
        return self.name
