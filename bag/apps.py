""" This is an import of app configuration from Django libraries """
from django.apps import AppConfig  # Import AppConfig from django.apps


class BagConfig(AppConfig):
    """ This class is used to build bag app using Django libraries """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
