from django.apps import AppConfig


class ZadanieAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop_app'

    def ready(self):
        import shop_app.signals
