from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class TasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"
    verbose_name = "Task Management"

    def ready(self):
        try:
            autodiscover_modules("signals")
        except ImportError as e:
            raise ImportError(f"Unable to load signals: {e}")
