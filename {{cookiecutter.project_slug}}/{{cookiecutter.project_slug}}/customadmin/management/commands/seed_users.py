import pandas as pd
from django.contrib.auth import get_user_model

from django.core.management.base import BaseCommand

# from django.contrib.auth.models import Group, Permission

def get_boolean(value):
    if not pd.isna(value):
        return bool(str(value).lower().title())
    return False


class Command(BaseCommand):
    help = "My shiny new management command."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        self.stdout.write("==> Seed Users")


        df = pd.read_csv("seed_data/users.csv")

        passwd = input("Enter a default pass for all users: ")

        for index, row in df.iterrows():
            print("-" * 80)
            email = row.get("email")
            username = row.get("username").strip() if not pd.isna(row.get("username")) else email

            instance = get_user_model().objects.create_user(username, email, passwd)
            instance.first_name = row.get("first_name", '').strip()
            instance.last_name = row.get("last_name", '').strip()
            instance.is_staff = get_boolean(row.get("is_staff"))
            instance.is_superuser = get_boolean(row.get("is_superuser"))
            instance.save()

            print(instance.last_name, instance.first_name)

        self.stdout.write(self.style.SUCCESS("DONE!"))
