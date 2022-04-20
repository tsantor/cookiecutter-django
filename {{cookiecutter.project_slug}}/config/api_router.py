from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
{%- if cookiecutter.use_simplejwt == "y" %}
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
{%- else %}
from rest_framework.authtoken.views import obtain_auth_token
{%- endif %}

{%- if cookiecutter.use_drf == 'y' %}
from rest_framework.authtoken.views import obtain_auth_token
{%- endif %}

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)


app_name = "api"
# urlpatterns = router.urls

urlpatterns = [
    # Place all your app's API URLS here.
    path("users/", include("{{ cookiecutter.project_slug }}.users.api.urls")),
    # Auth (https://www.django-rest-framework.org/api-guide/authentication/)
    {% if cookiecutter.use_simplejwt == "y" -%}
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    {%- else %}
    path("auth-token/", obtain_auth_token),
    {%- endif %}
    {% if cookiecutter.use_dj_rest_auth == "y" -%}
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    {%- endif %}
]
