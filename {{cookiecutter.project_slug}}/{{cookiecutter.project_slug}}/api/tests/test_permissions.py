import pytest

from ..permissions import IsSuperUser, IsActive

@pytest.mark.django_db
def test_is_super_user_permission(request_factory, user, superuser):
    # Simulate a request from a non-superuser
    request = request_factory.get('/')
    request.user = user
    permission = IsSuperUser()
    assert not permission.has_permission(request, None)

    # Simulate a request from a superuser
    request.user = superuser
    assert permission.has_permission(request, None)


@pytest.mark.django_db
def test_is_active_permission(request_factory, user, inactive_user):
    # Simulate a request from an inactive user
    request = request_factory.get('/')
    request.user = inactive_user
    permission = IsActive()
    assert not permission.has_permission(request, None)

    # Simulate a request from an active user
    request.user = user
    print(request.user.__dict__)
    assert permission.has_permission(request, None)
