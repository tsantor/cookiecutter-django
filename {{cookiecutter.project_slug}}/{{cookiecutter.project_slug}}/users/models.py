from django.contrib.auth.models import AbstractUser
from django.db.models import CharField{% if cookiecutter.username_type == "email" %}, EmailField{% endif %}
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
{%- if cookiecutter.username_type == "email" %}

from {{ cookiecutter.project_slug }}.users.managers import UserManager
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
    # first_name = None  # type: ignore
    # last_name = None  # type: ignore
    first_name = CharField(_("First Name"), blank=True, max_length=255)
    last_name = CharField(_("Last Name"), blank=True, max_length=255)

    @property
    def display_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.email:
            return self.email
        elif self.username:
            return self.username

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
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

    def __str__(self):
        """Return a string representation of this object for display."""
        return self.display_name

{% if cookiecutter.use_django_auditlog == "y" %}
auditlog.register(User)
{%- endif %}
