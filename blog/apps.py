""" Import Django libraries to create an app """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ Used Django build in libraries to create an app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
