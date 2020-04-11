from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand as DjangoBaseCommand

# from functools import wraps


# def verbose(func):
#     @wraps(func)
#     def wrapper(self, *args, **kwargs):
#         print("wrapped")
#         self.write_info(f"==> {self.msg}")
#         result = func(self, *args, **kwargs)
#         self.write_success(f"{self.msg} - DONE!")
#         return result

#     return wrapper


class BaseCommand(DjangoBaseCommand):
    help = "My shiny new management command."
    msg = None

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def write_info(self, msg):
        self.stdout.write(msg)

    def write_error(self, msg):
        self.stdout.write(self.style.ERROR(msg))

    def write_success(self, msg):
        self.stdout.write(self.style.SUCCESS(msg))

    def run_handle(self, *args, **options):
        raise NotImplementedError(
            "subclasses of BaseCommand must provide a run_handle() method"
        )

    def handle(self, *args, **options):
        if not self.msg:
            raise ImproperlyConfigured("msg must be set.")
        self.write_info(f"==> {self.msg}")
        self.run_handle(*args, **options)
        self.write_success(f"{self.msg} - DONE!")
