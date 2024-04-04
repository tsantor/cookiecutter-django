from {{ cookiecutter.project_slug }}.users.models import User

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_get_absolute_url(user: User):
    {%- if cookiecutter.username_type == "email" %}
    assert user.get_absolute_url() == f"/users/{user.pk}/"
    {%- else %}
    assert user.get_absolute_url() == f"/users/{user.username}/"
    {%- endif %}

# Forked additions
@pytest.mark.django_db()
def test_display_name_property():
    # Create a user with first name, last name, email, and username
    user = User.objects.create(name="John Doe", email="john.doe@example.com")

    # Assign user other possible properties
    user.first_name = "John"
    user.last_name = "Doe"
    user.username = "john.doe"

    assert user.display_name == "John Doe"

    # Remove the name
    user.name = ""

    assert user.display_name == "John Doe"

    # Remove first and last name
    user.first_name = ""
    user.last_name = ""
    user.save()

    assert user.display_name == "john.doe"

    # Remove the username
    user.username = ""

    assert user.display_name == "john.doe@example.com"

    # Remove the email
    user.email = ""

    assert user.display_name == "Anonymous"

@pytest.mark.django_db()
def test_initials_property():
    # Create a user with first name and last name
    user = User.objects.create(name="John Doe")

    assert user.initials == "JD"

    # Assign user other possible properties
    user.first_name = "John"
    user.last_name = "Doe"

    # Remove the name
    user.name = ""

    assert user.initials == "JD"

    # Remove first and last name
    user.first_name = ""
    user.last_name = ""

    assert user.initials == "??"

