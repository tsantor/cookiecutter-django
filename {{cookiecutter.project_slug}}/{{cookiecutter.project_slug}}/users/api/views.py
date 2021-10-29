from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from {{cookiecutter.project_slug}}.api.permissions import IsSuperUser

from .serializers import MyUserSerializer, UserSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
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

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return MySerializer
