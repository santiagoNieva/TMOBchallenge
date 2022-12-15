from django.apps import AppConfig


class RedirectionConfig(AppConfig):
    name = 'Redirection'

    def ready(self):
        import Redirection.signals
