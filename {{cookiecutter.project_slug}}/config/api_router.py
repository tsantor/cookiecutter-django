from django.conf import settings
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter
# from {{ cookiecutter.project_slug }}.users.api.views import UserViewSet
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
    # path("app1/", include("app1.api.urls")),
    # path("app2/", include("app2.api.urls")),
    path("users/", include("{{ cookiecutter.project_slug }}.users.api.urls")),

    path("auth-token/", obtain_auth_token),
    path("swagger/", get_swagger_view(title="Test API")),
]
