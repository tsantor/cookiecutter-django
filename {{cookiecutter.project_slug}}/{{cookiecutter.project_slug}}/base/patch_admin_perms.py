"""
Hide permission in the Django admin which are irrelevant, and not used at all.
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User


class PermissionFilterMixin(object):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name in ("permissions", "user_permissions"):
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            qs = _filter_permissions(qs)
            kwargs["queryset"] = qs

        return super().formfield_for_manytomany(
            db_field, request, **kwargs
        )


class MyGroupAdmin(PermissionFilterMixin, GroupAdmin):
    pass


class MyUserAdmin(PermissionFilterMixin, UserAdmin):
    pass

User = get_user_model()

# Override default registered Admin for User and Group
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
admin.site.register(Group, MyGroupAdmin)


def _filter_permissions(qs):
    # content_type__app_label__in, codename__in, codename__endswith
    return qs.exclude(content_type__app_label__in=settings.ADMIN_HIDE_PERMS)
