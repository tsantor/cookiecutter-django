from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    default_site = "{{ cookiecutter.project_slug }}.admin.admin.CustomAdminSite"
