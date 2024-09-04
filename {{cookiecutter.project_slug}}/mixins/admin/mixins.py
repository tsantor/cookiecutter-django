from django.http import HttpRequest

class ReadOnlyAdminMixin:
    """
    Mixin to make a model read-only in Django admin.
    """
    def has_add_permission(self, request: HttpRequest) -> bool:
        """
        Deny permission to add objects in Django admin.
        """
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        """
        Deny permission to change objects in Django admin.
        """
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        """
        Deny permission to delete objects in Django admin.
        """
        return False


class ChangeOnlyAdminMixin:
    """
    Mixin to allow only changing of a model in Django admin.
    """
    def has_add_permission(self, request: HttpRequest) -> bool:
        """
        Deny permission to add objects in Django admin.
        """
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        """
        Allow permission to change objects in Django admin.
        """
        return True

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        """
        Deny permission to delete objects in Django admin.
        """
        return False


class DeleteOnlyAdminMixin:
    """
    Mixin to allow only deletion of a model in Django admin.
    """
    def has_add_permission(self, request: HttpRequest) -> bool:
        """
        Deny permission to add objects in Django admin.
        """
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        """
        Deny permission to change objects in Django admin.
        """
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        """
        Allow permission to delete objects in Django admin.
        """
        return True


class ChangeDeleteOnlyAdminMixin:
    """
    Mixin to allow changing and deletion of a model in Django admin.
    """
    def has_add_permission(self, request: HttpRequest) -> bool:
        """
        Deny permission to add objects in Django admin.
        """
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        """
        Allow permission to change objects in Django admin.
        """
        return True

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        """
        Allow permission to delete objects in Django admin.
        """
        return True
