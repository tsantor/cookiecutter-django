# -*- coding: utf-8 -*-

from rest_framework import mixins, viewsets
# from ipware import get_client_ip


# class MyGenericViewSet(viewsets.GenericViewSet):
#     """Custom API response format."""

#     def initial(self, request, *args, **kwargs):

#         client_ip, _ = get_client_ip(request)
#         request.META["REMOTE_ADDR"] = client_ip

#         return super().initial(request, *args, **kwargs)

#     def get_request_ip_address(self):
#         return self.request.META.get("REMOTE_ADDR")

#     def get_request_endpoint_url(self):
#         return self.request.get_full_path()

#     def get_requet_method_type(self):
#         return self.request.method

#     def get_serializer_context(self):
#         """
#         Override to set IP Address and request url in context
#         """
#         ctx = super().get_serializer_context()

#         ctx["user"] = self.request.user
#         ctx["ip_address"] = self.get_request_ip_address()
#         ctx["endpoint_url"] = self.get_request_endpoint_url()
#         ctx["endpoint_name"] = self.get_view_name()

#         return ctx


class MyModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    MyGenericViewSet,
):
    """Custom API response format."""

    pass


class MyCreateViewSet(mixins.CreateModelMixin, MyGenericViewSet):
    """Custom API response format."""

    pass


class MyCreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, MyGenericViewSet
):
    """Custom API response format."""

    pass


class MyCreateRetrieveViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, MyGenericViewSet
):
    """Custom API response format."""

    pass


class MyCreateListRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    MyGenericViewSet,
):
    """Custom API response format."""

    pass


class MyListViewSet(mixins.ListModelMixin, MyGenericViewSet):
    """Custom API response format."""

    pass


class MyListUpdateViewSet(
    mixins.ListModelMixin, mixins.UpdateModelMixin, MyGenericViewSet
):
    """Custom API response format."""

    pass


class MyListRetrieveViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, MyGenericViewSet
):
    """Custom API response format."""

    pass


class MyRetrieveUpdateViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, MyGenericViewSet
):
    """Custom API response format."""

    pass


class MyRetrieveViewSet(mixins.RetrieveModelMixin, MyGenericViewSet):
    """Custom API response format."""

    pass


class MyUpdateViewSet(mixins.UpdateModelMixin, MyGenericViewSet):
    """Custom API response format."""

    pass


class MyCreateUpdateViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, MyGenericViewSet
):
    """Custom API response format."""

    pass
