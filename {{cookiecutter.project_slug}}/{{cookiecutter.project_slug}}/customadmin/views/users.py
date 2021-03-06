# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin

from {{ cookiecutter.project_slug }}.customadmin.mixins import HasPermissionsMixin
from {{ cookiecutter.project_slug }}.customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUpdateView,
    MyView,
)

from ..forms import MyUserChangeForm, MyUserCreationForm

User = get_user_model()

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class UserListView(MyListView):
    paginate_by = 25
    ordering = ["username"]
    model = User
    # queryset = model.objects.exclude(username="manifestingest")
    template_name = "customadmin/adminuser/user_list.html"
    permission_required = ("users.view_user",)


class UserCreateView(MyCreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = "customadmin/adminuser/user_form.html"
    permission_required = ("users.add_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class UserUpdateView(MyUpdateView):
    model = User
    form_class = MyUserChangeForm
    template_name = "customadmin/adminuser/user_form.html"
    permission_required = ("users.change_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class UserDeleteView(MyDeleteView):
    model = User
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("users.delete_user",)


class UserPasswordView(MyUpdateView):
    model = User
    form_class = AdminPasswordChangeForm
    template_name = "customadmin/adminuser/password_change_form.html"
    permission_required = ("users.change_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs['user'] = self.request.user
        kwargs["user"] = kwargs.pop("instance")
        return kwargs


class UserAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = User
    queryset = User.objects.all().order_by("last_name")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        # ctx.update({"obj": obj})
        # print(ctx)
        return t.render({"o": obj})

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search)
                | Q(first_name__icontains=self.search)
                | Q(last_name__icontains=self.search)
                # | Q(state__icontains=self.search)
                # | Q(year__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data
