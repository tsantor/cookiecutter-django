class ReadOnlyAdminMixin:
    """
    Mixin to make a model read-only in the Django admin.
    """

    def has_add_permission(self, request):
        """
        Return False to disable adding in the admin.
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Return False to disable editing in the admin.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Return False to disable deleting in the admin.
        """
        return False


class ChangeOnlyAdminMixin:
    """
    Mixin to allow only changing a model in the Django admin.
    """

    def has_add_permission(self, request):
        """
        Return False to disable adding in the admin.
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Return True to enable editing in the admin.
        """
        return True

    def has_delete_permission(self, request, obj=None):
        """
        Return False to disable deleting in the admin.
        """
        return False


class DeleteOnlyAdminMixin:
    """
    Mixin to allow only deleting a model in the Django admin.
    """

    def has_add_permission(self, request):
        """
        Return False to disable adding in the admin.
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Return False to disable editing in the admin.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Return True to enable deleting in the admin.
        """
        return True


class ChangeDeleteOnlyAdminMixin:
    """
    Mixin to allow only changing and deleting a model in the Django admin.
    """

    def has_add_permission(self, request):
        """
        Return False to disable adding in the admin.
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Return True to enable editing in the admin.
        """
        return True

    def has_delete_permission(self, request, obj=None):
        """
        Return True to enable deleting in the admin.
        """
        return True
