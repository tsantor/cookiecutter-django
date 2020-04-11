# -*- coding: utf-8 -*-

from django.urls import path

from .. import views

# -----------------------------------------------------------------------------

app_name = "adminuser"

urlpatterns = [
    # User
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/create/", views.UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path(
        "users/<int:pk>/password/",
        views.UserPasswordView.as_view(),
        name="user-password",
    ),
    path("ajax-users", views.UserAjaxPagination.as_view(), name="user-list-ajax"),
    # # Group
    # path("groups/", views.GroupListView.as_view(), name="group-list"),
    # path("groups/create/", views.GroupCreateView.as_view(), name="group-create"),
    # path(
    #     "groups/<int:pk>/update/", views.GroupUpdateView.as_view(), name="group-update"
    # ),
    # path(
    #     "groups/<int:pk>/delete/", views.GroupDeleteView.as_view(), name="group-delete"
    # ),
]

# -----------------------------------------------------------------------------
