import csv

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "My shiny new management command."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):

        results = get_user_model().objects.all()

        for r in results:
            # Normalize email
            r.username = r.email = r.username.lower()
            r.save()
