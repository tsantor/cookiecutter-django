# -*- coding: utf-8 -*-

from django.apps import AppConfig

# -----------------------------------------------------------------------------


class CustomAdminConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.customadmin"
    verbose_name = "Custom Admin"

    def ready(self):
        # Avoid AppRegistryNotReady exception
        # TODO: We may be able to eliminate this
        from . import monkey_patch
