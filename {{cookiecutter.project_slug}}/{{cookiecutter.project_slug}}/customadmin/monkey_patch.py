# -*- coding: utf-8 -*-

# NOTE: While monkey patching may be frowned upon, our use case here is OK
# as we're simply adding additional helper methods that will not affect
# future versions of Django if we were to upgrade.

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.urls import reverse

# -----------------------------------------------------------------------------
# Monkey patch User model
# -----------------------------------------------------------------------------


# def user_get_list_url(self):
#     return reverse("customadmin:users:user-list")


# def user_get_update_url(self):
#     return reverse("customadmin:users:user-update", kwargs={"pk": self.pk})


# def user_get_delete_url(self):
#     return reverse("customadmin:users:user-delete", kwargs={"pk": self.pk})


# def user_get_group_list(self):
#     """Return a comma separated list of group names for the User list in CMS"""
#     group_list = self.groups.values_list("name", flat=True)
#     return ", ".join(group_list)


# def user_str(self):
#     if self.first_name and self.last_name:
#         return f"{self.last_name}, {self.first_name}"
#     elif self.username:
#         return self.username
#     elif self.email:
#         return self.email


# get_user_model().add_to_class("get_list_url", user_get_list_url)
# get_user_model().add_to_class("get_update_url", user_get_update_url)
# get_user_model().add_to_class("get_delete_url", user_get_delete_url)
# get_user_model().add_to_class("get_group_list", user_get_group_list)
# get_user_model().add_to_class("__str__", user_str)

# -----------------------------------------------------------------------------
# Monkey patch Group model
# -----------------------------------------------------------------------------


# def group_get_list_url(self):
#     return reverse("customadmin:auth:group-list")


# def group_get_update_url(self):
#     return reverse("customadmin:auth:group-update", kwargs={"pk": self.pk})


# def group_get_delete_url(self):
#     return reverse("customadmin:auth:group-delete", kwargs={"pk": self.pk})


# Group.add_to_class("get_list_url", group_get_list_url)
# Group.add_to_class("get_update_url", group_get_update_url)
# Group.add_to_class("get_delete_url", group_get_delete_url)

# -----------------------------------------------------------------------------
# Monkey patch Permission model
# -----------------------------------------------------------------------------


def perm_str(self):
    return "%s | %s" % (self.content_type.app_label, self.name)


Permission.add_to_class("__str__", perm_str)
