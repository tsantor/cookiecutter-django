A collection of 3rd party package commands. You may or may not have these packages installed.

## Commands (one time)

- `create_periodic_tasks` - Creates Periodic Tasks that run at 4am daily.
- `create_robots` - Creates a typical robots.txt

## Commands (meant to be run daily)

- Delete Expired Sessions - Runs `clearsessions` for `sessions` app.
- Delete Expired Tokens - Runs `cleartokens` for `oauth2_provider` app.
- Delete Old Audit Logs - Runs `clean_apilogs` for `drf_api_logger` app.
- Delete Old API Logs - Runs `clean_auditlogs` for `auditlog` app.
- Delete Old Task Results - Runs `clean_taskresults` for `django_celery` app.
