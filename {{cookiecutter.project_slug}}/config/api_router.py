from django.conf import settings
from django.urls import include, path
from rest_framework import permissions
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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

{%- if cookiecutter.use_drf == 'y' %}
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
{%- endif %}

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)

schema_view = get_schema_view(
    openapi.Info(title="{{ cookiecutter.project_name }} API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    path("rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    {%- endif %}
    # Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # SpectacularAPI
    path("schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]
