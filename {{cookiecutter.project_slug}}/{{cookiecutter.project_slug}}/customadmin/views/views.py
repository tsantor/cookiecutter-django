# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# -----------------------------------------------------------------------------


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "customadmin/index.html"
