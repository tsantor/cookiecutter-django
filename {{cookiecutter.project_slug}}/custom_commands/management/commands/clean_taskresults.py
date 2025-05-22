import json
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django_celery.results.models import TaskResult


class Command(BaseCommand):
    help = "Deletes TaskResult instances older than a specified number of days"

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=90,
            required=False,
            help="Number of days to use as the cutoff for deleting task result entries",
        )

    def handle(self, *args, **kwargs):
        days = kwargs["days"]

        # Calculate the cutoff date
        cutoff_date = timezone.now() - timedelta(days=days)

        # Find and delete TaskResult instances older than the specified number of days
        old_entries = TaskResult.objects.filter(date_created__date__lt=cutoff_date)
        count = old_entries.count()
        old_entries.delete()

        # Output the result
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully deleted {count} task results older than {days} days"
            )
        )
        return json.dumps(
            {
                "message": f"Successfully deleted {count} task results older than {days} days",  # noqa: E501
                "total_deleted": count,
            }
        )
