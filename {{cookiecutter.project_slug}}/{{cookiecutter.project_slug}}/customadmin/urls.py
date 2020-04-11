# -*- coding: utf-8 -*-

from django.urls import path, include

from . import auth_urls, views, urls_user, urls_group

# -----------------------------------------------------------------------------

app_name = "customadmin"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("auth/", include(urls_user, namespace="users")),
    path("auth/", include(urls_group, namespace="auth")),
    # path("", include("usign.core.urls", namespace="core")),
    # Auth URLs
    path("", include(auth_urls)),
]

# -----------------------------------------------------------------------------
