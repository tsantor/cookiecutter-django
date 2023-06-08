from django_otp.admin import OTPAdminSite

# from django.contrib import admin


class CustomAdminSite(OTPAdminSite):
    # class CustomAdminSite(admin.AdminSite):
    site_title = "{{ cookiecutter.project_name }}"
    site_header = "{{ cookiecutter.project_name }}"
    index_title = "{{ cookiecutter.project_name }} Administration"
    enable_nav_sidebar = False