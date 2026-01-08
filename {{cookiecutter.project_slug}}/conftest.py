import tempfile

import pytest
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.tests.factories import UserFactory

# from django.contrib.auth import get_user_model  # noqa: ERA001

# User = get_user_model()  # noqa: ERA001

@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


# -----------------------------------------------------------------------------
# My forked additions
# -----------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def _media_storage(settings):
    settings.MEDIA_ROOT = tempfile.mkdtemp()


@pytest.fixture(autouse=True)
def _static_storage(settings):
    settings.STATIC_ROOT = tempfile.mkdtemp()


@pytest.fixture
def user2():
    return User.objects.create_user(
        {%- if cookiecutter.username_type == "username" %}
        username="user@test.com",
        {%- endif -%}
        email="user@test.com",
        password="testpass",  # noqa: S106
    )


@pytest.fixture
def staff():
    return User.objects.create_user(
        {%- if cookiecutter.username_type == "username" %}
        username="staff@test.com",
        {%- endif -%}
        email="staff@test.com",
        password="testpass",  # noqa: S106
        is_staff=True,
    )


@pytest.fixture
def superuser():
    return User.objects.create_user(
        {%- if cookiecutter.username_type == "username" %}
        username="superuser@test.com",
        {%- endif -%}
        email="superuser@test.com",
        password="testpass",  # noqa: S106
        is_superuser=True,
        is_staff=True,
    )


@pytest.fixture
def inactive_user():
    return User.objects.create_user(
        {%- if cookiecutter.username_type == "username" %}
        username="inactiveuser@test.com",
        {%- endif -%}
        email="inactiveuser@test.com",
        password="testpass",  # noqa: S106
        is_active=False,
    )

@pytest.fixture
def non_superuser():
    return User.objects.create_user(
        {%- if cookiecutter.username_type == "username" %}
        username="nonsuperuser@test.com",
        {%- endif -%}
        email="nonsuperuser@test.com",
        password="testpass",  # noqa: S106
        is_superuser=False,
        is_staff=True,
    )


@pytest.fixture
def request_factory():
    return APIRequestFactory()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_client(api_client, user):
    """
    Standard DRF way to authenticate a client.
    This works perfectly with Allauth and standard Django sessions.
    """
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def staff_authenticated_client(api_client, staff):
    api_client.force_authenticate(user=staff)
    return api_client


@pytest.fixture
def superuser_authenticated_client(api_client, superuser):
    api_client.force_authenticate(user=superuser)
    return api_client
