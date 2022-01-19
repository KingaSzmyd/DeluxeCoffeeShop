from django.db import models
from django.core.validators import MaxLengthValidator

from django.contrib.auth.models import User
from products.models import Product


# Create your models here.


class Review(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(validators=[MaxLengthValidator(500)])
    date_posted = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return '{} by {}'.format(self.body, self.username)
        