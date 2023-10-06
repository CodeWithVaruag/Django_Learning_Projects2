from django.apps import AppConfig


class App2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app2'

class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app2'