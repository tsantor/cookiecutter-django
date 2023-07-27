from celery import shared_task
from django.core import management


@shared_task
def delete_expired_tokens():
    """Delete expired oAuth tokens"""
    management.call_command("cleartokens", verbosity=0)


@shared_task
def delete_expired_sessions():
    """Delete expired sessions"""
    management.call_command("clearsessions", verbosity=0)
