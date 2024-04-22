from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from .forms import UserAdminChangeForm
from .forms import UserAdminCreationForm
from .models import User

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.site.login = login_required(admin.site.login)  # type: ignore[method-assign]


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        {%- if cookiecutter.username_type == "email" %}
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        {%- else %}
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        {%- endif %}
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = [
        "{{cookiecutter.username_type}}",
        "name",
        "is_superuser",
        "is_staff",
        "is_superuser",
        "last_login",
    ]
    search_fields = ["name"]
    {%- if cookiecutter.username_type == "email" %}
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    {%- endif %}

    # Forked additions - keeps diffs minimal
    def get_fieldsets(self, request, obj=None):
        """Remove some fieldsets based on the user permissions."""
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            fieldsets = tuple(
                (name, options)
                for name, options in fieldsets
                if name not in ["Permissions", "Important dates"]
            )
        return fieldsets

    def get_form(self, request, obj=None, **kwargs):
        """Disable some fields based on the user permissions."""
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        # Prevent non-superusers from editing any permissions
        # These fields only exist when editing an existing user
        if obj and not is_superuser:
            disabled_fields |= {
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
                "last_login",
                "date_joined",
            }
            for f in disabled_fields:
                field = form.base_fields.get(f)
                if field:
                    field.disabled = True

        return form
