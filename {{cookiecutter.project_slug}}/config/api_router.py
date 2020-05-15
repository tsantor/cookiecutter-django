from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
{%- if cookiecutter.use_drf_jwt == "y" %}
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
{%- else %}
from rest_framework.authtoken.views import obtain_auth_token
{%- endif %}
from rest_framework_swagger.views import get_swagger_view

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
    path("swagger/", get_swagger_view(title="{{ cookiecutter.project_name }} API")),
]
