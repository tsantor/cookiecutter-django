from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        """Return a string representation of this object for display."""
        if self.first_name and self.last_name:
            return f"{self.last_name}, {self.first_name}"
        elif self.username:
            return self.username
        elif self.email:
            return self.email
