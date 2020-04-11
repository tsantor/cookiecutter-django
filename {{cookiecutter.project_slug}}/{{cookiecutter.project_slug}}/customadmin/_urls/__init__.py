# -*- coding: utf-8 -*-
from django.urls import include, path
from .auth_urls import urlpatterns as auth_urls
from .urls_group import urlpatterns as urls_group
from .urls_user import urlpatterns as urls_user

from .. import views

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

