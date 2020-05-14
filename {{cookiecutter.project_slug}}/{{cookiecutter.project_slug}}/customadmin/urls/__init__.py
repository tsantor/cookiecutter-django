# -*- coding: utf-8 -*-
from django.urls import include, path

from .. import views
from .auth import urlpatterns as auth_urls
from .groups import urlpatterns as group_urls
from .users import urlpatterns as user_urls

# -----------------------------------------------------------------------------

app_name = "customadmin"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("users/", include((user_urls, "users"))),
    path("groups/", include((group_urls, "auth"))),
    # path("", include(("{{ cookiecutter.project_slug }}.core.urls", "core"))),
    # Auth URLs
    path("", include(auth_urls)),
]
