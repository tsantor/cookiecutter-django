from django.conf import settings
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from {{ cookiecutter.project_slug }}.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)

app_name = "api"

# urlpatterns = router.urls  # noqa: ERA001

# Forked additions - keeps diffs minimal
urlpatterns = [
    # Place all your app's API URLS here.
    path("users/", include("{{ cookiecutter.project_slug }}.users.api.urls")),
    # Auth (https://www.django-rest-framework.org/api-guide/authentication/)
]
