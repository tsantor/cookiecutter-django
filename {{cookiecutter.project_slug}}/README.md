# {{ cookiecutter.project_name }}

## Tech Stack

- Ubuntu 18.04 LTS
- Django 3
- Python 3.8
- Nginx
- Gunicorn
- PostgreSQL
- Redis
- Celery
- Supervisor


### Clone the Repo
```
git clone https://bitbucket.org/xstudios/{{ cookiecutter.project_slug }}
```

## Create a Development Environment using Docker

```
docker-compose -f local.yml up
```

## Development App

You can then access the site at `http://localhost:3000/` and the BrowserSync GUI at `http://localhost:3001`. Other URLs of note:

- `http:://localhost:3000/admin/` - Django Admin
- `http:://localhost:3000/customadmin/` - Custom Admin built using Inspinia theme that we use for client facing CMS/Admins.
- `http:://localhost:3000/api/v1/swagger/` - Swagger API

{% if cookiecutter.use_mailhog == "y" %}
## Email Server
In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``
{% endif %}

{% if cookiecutter.use_celery == "y" %}

## Celery
This app comes with Celery.

To run a celery worker:

```
cd {{cookiecutter.project_slug}}
celery -A config.celery_app worker -l info
```

> Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.
{% endif %}


{% if cookiecutter.use_sentry == "y" %}

## Sentry
Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.
{% endif %}

## Basic Commands

### Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy {{cookiecutter.project_slug}}

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Running tests with py.test

    $ pytest
