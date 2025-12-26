from django.apps import AppConfig


class ActivitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'activities'

    def ready(self):
        # Import signal handlers to connect them
        from . import signals  # noqa: F401
