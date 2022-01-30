""" Import app configuration from Django """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Configurate the checkout app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals  # noqa  # pylint: disable=unused-import
        # pylint: disable=import-outside-toplevel
