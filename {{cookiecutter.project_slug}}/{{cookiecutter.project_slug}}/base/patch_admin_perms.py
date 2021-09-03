"""
Hide permission in the Django admin which are irrelevant, and not used at all.
"""
import logging

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django.utils.module_loading import import_string

from {{ cookiecutter.project_slug }}.users.admin import UserAdmin

User = get_user_model()
logger = logging.getLogger(__name__)


def _filter_permissions(qs):
    # content_type__app_label__in, codename__in, codename__endswith
    qs = qs.exclude(content_type__app_label__in=settings.ADMIN_PATCH["HIDE_APPS"])
    if settings.ADMIN_PATCH["HIDE_PERMS"]:
        qs = qs.exclude(codename__in=settings.ADMIN_PATCH["HIDE_PERMS"])
    return qs


class PermissionFilterMixin(object):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name in ("permissions", "user_permissions"):
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            qs = _filter_permissions(qs)
            kwargs["queryset"] = qs

        return super().formfield_for_manytomany(db_field, request, **kwargs)


class MyGroupAdmin(PermissionFilterMixin, GroupAdmin):
    pass


class MyUserAdmin(PermissionFilterMixin, UserAdmin):
    pass


# Override default registered Admin for User and Group
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
admin.site.register(Group, MyGroupAdmin)

# Unregister models
if hasattr(settings, "ADMIN_PATCH"):
    for m in settings.ADMIN_PATCH["UNREGISTER_MODELS"]:
        try:
            model = import_string(m)
            admin.site.unregister(model)
        except (ModuleNotFoundError, RuntimeError) as e:
            logger.warning(
                str(e)
                + " Ensure the module is installed and/or added to INSTALLED_APPS if need be."
            )  # noqa

