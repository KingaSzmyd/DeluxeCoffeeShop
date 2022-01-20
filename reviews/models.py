from django.db import models
from django.core.validators import MaxLengthValidator
from django.utils.text import slugify

from django.contrib.auth.models import User


# Create your models here.


class ReviewPost(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_post")
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True) 
    body = models.TextField(validators=[MaxLengthValidator(500)])
    date_posted = models.DateTimeField(db_index=True, auto_now_add=True)
    
    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return '{} by {}'.format(self.body, self.username)
