import tempfile

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.tests.factories import UserFactory

# from django.contrib.auth import get_user_model  # noqa: ERA001

# User = get_user_model()  # noqa: ERA001

@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
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


@pytest.fixture()
def user2():
    return User.objects.create_user(
        {%- if cookiecutter.username_type == "username" %}
        username="user@test.com",
        {%- endif -%}
        email="user@test.com",
        password="testpass",  # noqa: S106
    )


@pytest.fixture()
def staff():
    return User.objects.create_user(
        {%- if cookiecutter.username_type == "username" %}
        username="staff@test.com",
        {%- endif -%}
        email="staff@test.com",
        password="testpass",  # noqa: S106
        is_staff=True,
    )


@pytest.fixture()
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


@pytest.fixture()
def inactive_user():
    return User.objects.create_user(
        {%- if cookiecutter.username_type == "username" %}
        username="inactiveuser@test.com",
        {%- endif -%}
        email="inactiveuser@test.com",
        password="testpass",  # noqa: S106
        is_active=False,
    )

@pytest.fixture()
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


@pytest.fixture()
def request_factory():
    return APIRequestFactory()


@pytest.fixture()
def api_client():
    return APIClient()


def get_jwt_token(api_client, target_user) -> str:
    """Get a JWT token for the target user."""
    url = reverse("api:rest_login")
    data = {"email": target_user.email, "password": "testpass"}
    response = api_client.post(url, data)
    return response.data.get("access")


def inject_token(api_client, target_user):
    """Inject the JWT token into the API client."""
    token = get_jwt_token(api_client, target_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


@pytest.fixture()
def authenticated_client(api_client, user):
    """Authenticate the API client with the test user."""
    {%- if cookiecutter.username_type == "username" %}
    api_client.login(username=user.username, password="testpass")  # noqa: S106
    {%- else %}
    api_client.login(email=user.email, password="testpass")  # noqa: S106
    {%- endif %}
    # api_client.force_authenticate(user=user)  # noqa: ERA001
    return inject_token(api_client, user)

@pytest.fixture()
def staff_authenticated_client(api_client, staff):
    """Authenticate the API client with the test user."""
    {%- if cookiecutter.username_type == "username" %}
    api_client.login(username=staff.username, password="testpass")  # noqa: S106
    {%- else %}
    api_client.login(email=staff.email, password="testpass")  # noqa: S106
    {%- endif %}
    return inject_token(api_client, staff)


@pytest.fixture()
def superuser_authenticated_client(api_client, superuser):
    """Authenticate the API client with the test user."""
    {%- if cookiecutter.username_type == "username" %}
    api_client.login(username=superuser.username, password="testpass")  # noqa: S106
    {%- else %}
    api_client.login(email=superuser.email, password="testpass")  # noqa: S106
    {%- endif %}
    return inject_token(api_client, superuser)
