{%- if cookiecutter.username_type == "email" %}
from typing import ClassVar

{% endif -%}
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
{%- if cookiecutter.username_type == "email" %}
from django.db.models import EmailField
{%- endif %}
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
{%- if cookiecutter.username_type == "email" %}

from .managers import UserManager
{%- endif %}

{%- if cookiecutter.use_django_auditlog == "y" %}
from auditlog.registry import auditlog
{%- endif %}


class User(AbstractUser):
    """
    Default custom user model for {{cookiecutter.project_name}}.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    {%- if cookiecutter.username_type == "email" %}
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore[assignment]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()
    {%- endif %}

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        {%- if cookiecutter.username_type == "email" %}
        return reverse("users:detail", kwargs={"pk": self.id})
        {%- else %}
        return reverse("users:detail", kwargs={"username": self.username})
        {%- endif %}

    # Forked additions - keeps diffs minimal
    @property
    def display_name(self) -> str:
        """Order of preference for user's display name."""
        if hasattr(self, "name") and self.name:
            return self.name
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}".strip()
        if hasattr(self, "username") and self.username:
            return self.username
        if self.email:
            return self.email
        return "Anonymous"

    @property
    def initials(self) -> str:
        def extract_and_capitalize(name):
            return ''.join(word[0].upper() for word in name.split())

        if hasattr(self, "name") and self.name:
            return extract_and_capitalize(self.name)
        if hasattr(self, "first_name") and hasattr(self, "last_name"):
            first_name = self.first_name[0] if self.first_name else "?"
            last_name = self.last_name[0] if self.last_name else "?"
            return f"{first_name}{last_name}".upper()
        return "??"

    def __str__(self):
        """Return a string representation of this object for display."""
        return self.display_name

{% if cookiecutter.use_django_auditlog == "y" %}
auditlog.register(User)
{%- endif %}
