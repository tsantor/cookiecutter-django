# -*- coding: utf-8 -*-
from usign.customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyUpdateView,
)
from django.contrib.auth.models import Group

from ..forms import MyGroupForm

# -----------------------------------------------------------------------------
# Groups
# -----------------------------------------------------------------------------


class GroupListView(MyListView):
    # paginate_by = 25
    model = Group
    template_name = "customadmin/adminuser/group_list.html"
    permission_required = ("auth.view_group",)


class GroupCreateView(MyCreateView):
    model = Group
    form_class = MyGroupForm
    template_name = "customadmin/adminuser/group_form.html"
    permission_required = ("auth.add_group",)


class GroupUpdateView(MyUpdateView):
    model = Group
    form_class = MyGroupForm
    template_name = "customadmin/adminuser/group_form.html"
    permission_required = ("auth.change_group",)


class GroupDeleteView(MyDeleteView):
    model = Group
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("auth.delete_group",)
