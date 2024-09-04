from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAdminUser


class IsSuperUser(IsAdminUser):
    """
    Permission class to check if the user is a superuser.
    Inherits from IsAdminUser to reuse the admin check logic.
    """

    def has_permission(self, request, view) -> bool:
        """
        Overridden method from IsAdminUser.
        Checks if the user in the request is a superuser.

        Args:
            request: The current request instance.
            view: The view which is being accessed.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        has_perm = super().has_permission(request, view)
        return bool(has_perm and request.user.is_superuser)


class IsActive(BasePermission):
    """
    Permission class to check if the user is active.
    """

    def has_permission(self, request, view) -> bool:
        """
        Checks if the user in the request is active.

        Args:
            request: The current request instance.
            view: The view which is being accessed.

        Returns:
            bool: True if the user is active, False otherwise.
        """
        return bool(request.user and request.user.is_active)
