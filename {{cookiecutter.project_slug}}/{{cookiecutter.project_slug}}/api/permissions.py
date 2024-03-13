# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission, IsAdminUser


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsActive(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)
