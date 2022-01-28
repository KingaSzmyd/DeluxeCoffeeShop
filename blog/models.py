from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField()
    body = models.TextField()
    date_posted = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']
  
    def __str__(self):
        return self.title
        

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                             related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(validators=[MaxLengthValidator(500)])
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return '{} by {}'.format(self.body, self.username)
