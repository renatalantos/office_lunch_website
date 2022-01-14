from django.apps import AppConfig


class TillConfig(AppConfig):
    name = 'till'

    def ready(self):
        import till.signals