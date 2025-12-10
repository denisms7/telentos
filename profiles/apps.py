from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
    verbose_name = 'Perfis de Usuário'

    def ready(self):
        import profiles.signals  # noqa: F401
