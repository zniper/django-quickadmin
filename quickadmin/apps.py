from django.apps import AppConfig


class QAdminAppConfig(AppConfig):
    name = 'quickadmin'
    verbose_name = 'Quick Admin'

    def ready(self):
        from .register import register_models
        register_models()
