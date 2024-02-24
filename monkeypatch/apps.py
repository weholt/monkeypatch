from django.apps import AppConfig


class MonkeypatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monkeypatch'
