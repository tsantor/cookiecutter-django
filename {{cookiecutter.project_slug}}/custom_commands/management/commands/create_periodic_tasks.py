from django.conf import settings
from django.core.management.base import BaseCommand
from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import PeriodicTask


def create_crontab():
    """Create a crontab schedule for 4am if it does not already exist."""
    return CrontabSchedule.objects.get_or_create(
        minute="0",
        hour="4",
        day_of_week="*",
        day_of_month="*",
        month_of_year="*",
        timezone=settings.TIME_ZONE,
    )


def create_periodic_task(crontab_schedule, name, task):
    """Create a periodic task if it does not already exist."""
    return PeriodicTask.objects.get_or_create(
        crontab=crontab_schedule,
        name=name,
        task=task,
    )


TASKS = [
    ("Delete Expired Sessions", "custom_commands.tasks.delete_expired_sessions"),
    ("Delete Expired Tokens", "custom_commands.tasks.delete_expired_tokens"),
    ("Delete Old Audit Logs", "custom_commands.tasks.delete_old_audit_logs"),
    ("Delete Old API Logs", "custom_commands.tasks.delete_old_api_logs"),
    ("Delete Old Task Results", "custom_commands.tasks.delete_old_api_logs"),
]


class Command(BaseCommand):
    help = "Create periodic tasks for typical things we do."

    def handle(self, *args, **kwargs):
        # Create a cron schedule
        crontab_schedule, created = create_crontab()
        if created:
            self.stdout.write(
                self.style.SUCCESS("Created crontab schedule for 4am daily."),
            )
        else:
            self.stdout.write(
                self.style.WARNING("Crontab schedule for 4am daily exists."),
            )

        # Create tasks
        for name, task in TASKS:
            _, created = create_periodic_task(crontab_schedule, name, task)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created periodic task "{name}".')
                )
            else:
                self.stdout.write(self.style.WARNING(f'Periodic task "{name}" exists.'))

        self.stdout.write(self.style.SUCCESS("Successfully created periodic tasks."))
