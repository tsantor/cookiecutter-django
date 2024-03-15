# Cookiecutter Django

This forked version of the [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) repo retains all the features of that repo and adds additional optional features to get started on more complex projects quickly.

## Features
- Makefile with some helpful commands
- Custom AdminSite class
- Custom Storage classes
- Prebuilt Celery Tasks
- Custom JSONRenderer (consistent DRF response format)
- Simple Model Mixins
- Simple Admin Mixins
- Bash Utility Scripts
  - Create User
  - Install Docker
- Traefik
  - Dashboard enabled (traefik.domain.com/)
  - Access log enabled
- Prometheus (prometheus.domain.com/)
- Grafana (grafana.domain.com/)
  - You will need to add your own dash (eg - Dashboard ID `XXX` Traefik official)

## Optional Integrations
These features can be enabled during initial project setup.
- Mosquitto service
- Prometheus service
- Grafana service
- Nginx integration for static file serving (via Traefix proxy)
  - This is preferabe to `whitenoise` - truly, don't ask!
- `dj-rest-auth` package (see known issues below)
- `django-auditlog` package
- `django-celery-results` package
- `django-oauth-toolkit` package
- `django-perm-filter` package
- `django-robots` package
- `djangorestframework-simplejwt` package
<!-- - `django-spaday` package -->


## Usage
```
cookiecutter https://github.com/tsantor/cookiecutter-django
```
You'll be prompted for some values. Provide them, then a Django project will be created for you.

## Production Deployment via Docker

Create the following DNS records:

- domain.com
- traefik.domain.com
- flower.domain.com (if opted for celery)
- prometheus.domain.com (if opted for prometheus)
- grafana.domain.com (if opted for grafana)


- On local machine run, `make rsync_to_prod`
- On production, run `make nginx_htaccess` - this
- On production, run `make traefik_htaccess`
- On production, run `make deploy_prod`


## Known issues
- Enabling `dj-rest-auth` will throw an error as it is not compatible with django-allauth > 0.54.0

## TODO
- Need to make work with frontend pipelines other than Gulp
- Move `api` to a package or packages
- Move `helpers` to a package or packages
- Move `mixins` to a package or packages
