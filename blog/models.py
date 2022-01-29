""" Import from the Django database """
from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    """ The Blog post model """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField()
    body = models.TextField()
    date_posted = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        """ The blog posts displaying ordering """
        ordering = ['-date_posted']

    def __str__(self):
        """ Function returning to the Blog post """
        return str(self.title)


class Comment(models.Model):
    """ The comments model"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                             related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(validators=[MaxLengthValidator(500)])
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ The comments displaying ordering """
        ordering = ['-date_posted']

    def __str__(self):
        return '{} by {}'.format(self.body, self.username)
        # pylint: disable=consider-using-f-string
