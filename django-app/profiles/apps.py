from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    name = "profiles"
    verbose_name = "Profiles"

    def ready(self):
        from . import hooks
