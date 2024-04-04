from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from {{ cookiecutter.project_slug }}.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet)

app_name = "api"

# urlpatterns = router.urls

# Forked additions - keeps diffs minimal
urlpatterns = [
    # Place all your app's API URLS here.
    path("users/", include("{{ cookiecutter.project_slug }}.users.api.urls")),
    # Auth (https://www.django-rest-framework.org/api-guide/authentication/)
    {% if cookiecutter.use_dj_rest_auth == "y" -%}
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    {%- endif %}
]
