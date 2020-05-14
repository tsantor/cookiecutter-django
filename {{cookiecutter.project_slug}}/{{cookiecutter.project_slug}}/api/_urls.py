# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view

# from .views import MyObtainAuthToken

# -----------------------------------------------------------------------------

app_name = "api"

urlpatterns = [
    # Place all your app's API URLS here.
    path("core/", include("{{ cookiecutter.project_slug }}.core.api.urls")),
    # Auth
    # path("api-token-auth/", MyObtainAuthToken.as_view()),
    path("api-token-auth/", obtain_auth_token),
    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),
    path("swagger/", get_swagger_view(title="{{ cookiecutter.project_name }} API")),
]
