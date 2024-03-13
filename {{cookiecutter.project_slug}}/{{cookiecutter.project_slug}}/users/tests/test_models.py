from {{ cookiecutter.project_slug }}.users.models import User

import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

def test_user_get_absolute_url(user: User):
    {%- if cookiecutter.username_type == "email" %}
    assert user.get_absolute_url() == f"/users/{user.pk}/"
    {%- else %}
    assert user.get_absolute_url() == f"/users/{user.username}/"
    {%- endif %}
@pytest.mark.django_db
def test_display_name_property():
    # Create a user with first name, last name, email, and username
    user = User.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com', username='johndoe')

    # Check that the name property returns the correct value
    assert user.display_name == 'John Doe'

    # Remove the first name and last name
    user.first_name = ''
    user.last_name = ''
    user.save()

    # Check that the name property now returns the email
    assert user.display_name == 'john.doe@example.com'

    # Remove the email
    user.email = ''
    user.save()

    # Check that the name property now returns the username
    assert user.display_name == 'johndoe'

    # Remove the username
    # delattr(user, 'username')

    # Check that the name property now returns 'Anonymous'
    # assert user.display_name == 'Anonymous'

@pytest.mark.django_db
def test_initials_property():
    # Create a user with first name and last name
    user = User.objects.create(first_name='John', last_name='Doe')

    # Check that the initials property returns the correct value
    assert user.initials == 'JD'

    # Remove the first name
    user.first_name = ''
    user.save()

    # Check that the initials property now returns '?D'
    assert user.initials == '?D'

    # Remove the last name
    user.last_name = ''
    user.save()

    # Check that the initials property now returns '??'
    assert user.initials == '??'
