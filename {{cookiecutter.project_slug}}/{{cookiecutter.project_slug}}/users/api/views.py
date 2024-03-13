from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from {{ cookiecutter.project_slug }}.users.models import User
from {{cookiecutter.project_slug}}.api.permissions import IsSuperUser

from .serializers import UserSerializer, MyUserSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    {%- if cookiecutter.username_type == "email" %}
    lookup_field = "pk"
    {%- else %}
    lookup_field = "username"
    {%- endif %}

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
# -----------------------------------------------------------------------------
# My forked version
# -----------------------------------------------------------------------------


class MyUserViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    """
    list:
    List all User

    create:
    Create a User

    retrieve:
    Get a User

    update:
    Update a User

    delete:
    Delete a User
    """

    queryset = User.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = (IsSuperUser,)
