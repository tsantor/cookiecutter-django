# -*- coding: utf-8 -*-

from django.urls import path

from . import views

# -----------------------------------------------------------------------------

app_name = "auth"

urlpatterns = [
    # Group
    path("groups/", views.GroupListView.as_view(), name="group-list"),
    path("groups/create/", views.GroupCreateView.as_view(), name="group-create"),
    path(
        "groups/<int:pk>/update/", views.GroupUpdateView.as_view(), name="group-update"
    ),
    path(
        "groups/<int:pk>/delete/", views.GroupDeleteView.as_view(), name="group-delete"
    ),
    # path("ajax-groups", views.GroupAjaxPagination.as_view(), name="group-list-ajax"),
]

# -----------------------------------------------------------------------------
