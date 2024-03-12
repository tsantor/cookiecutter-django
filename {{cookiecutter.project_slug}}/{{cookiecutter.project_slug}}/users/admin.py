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
        (_("Personal info"), {"fields": ("name", "first_name", "last_name")}),
        {%- else %}
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
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
    list_display = ["{{cookiecutter.username_type}}", "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "last_login",]
    search_fields = ["first_name", "last_name", "email"]
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

    def get_form(self, request, obj=None, **kwargs):
        """Determine which fields to disable based on the user's permissions."""
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        # Prevent non-superusers from editing any permissions
        if not is_superuser:
            disabled_fields |= {
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
                "last_login",
                "date_joined",
            }

        # Prevent non-superusers from editing their own permissions
        # if obj == request.user:
        #     disabled_fields |= {}

        for f in disabled_fields & form.base_fields.keys():
            form.base_fields[f].disabled = True

        return form
