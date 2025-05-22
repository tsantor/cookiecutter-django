import json

from celery import shared_task
from django.core import management


@shared_task
def delete_expired_tokens():
    """Delete expired oAuth tokens for`oauth2_provider` app."""
    management.call_command("cleartokens", verbosity=0)


@shared_task
def delete_expired_sessions():
    """Delete expired sessions for `sessions` app."""
    management.call_command("clearsessions", verbosity=0)


@shared_task
def delete_old_audit_logs(days: int = 90):
    """Delete audit logs older than X days for `auditlog` app."""
    return json.loads(
        management.call_command("clean_auditlogs", verbosity=0, days=days),
    )


@shared_task
def delete_old_api_logs(days: int = 90):
    """Delete API logs older than X days for `drf_api_logger` app."""
    return json.loads(management.call_command("clean_apilogs", verbosity=0, days=days))


@shared_task
def delete_old_api_task_results(days: int = 90):
    """Delete Task Results older than X days for `drf_api_logger` app."""
    return json.loads(
        management.call_command("clean_taskresults", verbosity=0, days=days)
    )
