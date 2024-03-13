# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# -----------------------------------------------------------------------------

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r"", views.MyUserViewSet, basename="user")


urlpatterns = [path("", include(router.urls))]
