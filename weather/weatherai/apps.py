from django.apps import AppConfig


class WeatheraiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weatherai'


class ThemeConfig(AppConfig):
    name = 'theme'