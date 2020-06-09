from django.conf import settings
from django.urls import include, path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter, SimpleRouter
{%- if cookiecutter.use_drf_jwt == "y" %}
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
{%- else %}
from rest_framework.authtoken.views import obtain_auth_token
{%- endif %}
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

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
    {% if cookiecutter.use_drf_jwt == "y" -%}
    path("api-token-auth/", obtain_jwt_token),
    path("api-token-refresh/", refresh_jwt_token),
    {%- else %}
    path("auth-token/", obtain_auth_token),
    {%- endif %}
    {% if cookiecutter.use_django_rest_auth == "y" -%}
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    {%- endif %}
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
