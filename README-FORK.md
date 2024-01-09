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
  - Dashboard enabled (traefik.domain.com/dashboard)
  - Access log enabled


## Optional Integrations
These features can be enabled during initial project setup.
- Mosquitto service
- Nginx integration for static file serving (via Traefix proxy)
- `django-robots` package
- `dj-rest-auth` package (see known issues below)
- `djangorestframework-simplejwt` package
- `django-oauth-toolkit` package
- `django-auditlog` package
- `django-celery-results` package
- `django-perm-filter` package


## Usage
```
cookiecutter https://github.com/tsantor/cookiecutter-django
```
You'll be prompted for some values. Provide them, then a Django project will be created for you.


## Production Deployment via Docker

- On local machine run, `push_production_env`
- On production, run `make nginx_htaccess` - this
- On production, run `make traefik_htaccess`
- On production, run `make deploy_prod`


## Known issues
- Enabling rest-auth will thrown an error as it is not compatible with django-allauth > 0.54.0

## TODO
- Need to make work with frontend pipelines other than Gulp
