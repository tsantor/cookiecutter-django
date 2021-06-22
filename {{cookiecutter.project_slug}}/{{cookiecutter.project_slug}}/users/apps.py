from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import {{ cookiecutter.project_slug }}.users.signals  # noqa F401
        except ImportError:
            pass
        from {{ cookiecutter.project_slug }}.base import patch_admin_perms  # noqa F401
        from {{ cookiecutter.project_slug }}.base import patch_admin  # noqa F401
