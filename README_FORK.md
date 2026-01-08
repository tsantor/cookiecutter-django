# Cookiecutter Django

This forked version of the [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) repo retains all the features of that repo and adds additional optional features to get started on more complex projects quickly. This is a **VERY OPINIONATED** fork so be aware.

## Features

- Makefile with tons of helpful commands
- Custom AdminSite class
- Custom Storage classes
- Prebuilt Celery Tasks
- Custom JSONRenderer (consistent DRF response format)
- Simple Mixins

## Features if Docker option used:

- Bash Utility Scripts
  - Create User
  - Install Docker
- Traefik
  - Dashboard enabled (traefik.domain.com/dashboard/)
  - Access log enabled
  - Metrics enabled
- Prometheus (prometheus.domain.com/)
- Grafana (grafana.domain.com/)
  - You will need to add your own dash (eg - Dashboard ID `XXX` Traefik official)

## Optional Integrations

These features can be enabled during initial project setup.

- Mosquitto service
- Prometheus service
- Grafana service
- Nginx integration for static file serving (via Traefix proxy)
  - This is preferabe to `whitenoise`
- `django-auditlog` package
- `django-celery-results` package
- `django-oauth-toolkit` package
- `django-perm-filter` package
- `django-robots` package
- `drf-api-logger` package

## Usage

```
cookiecutter https://github.com/tsantor/cookiecutter-django
```

You'll be prompted for some values. Provide them, then a Django project will be created for you.

## TODO

- Move `api` to a package or packages
- Move `helpers` to a package or packages
- Move `mixins` to a package or packages
