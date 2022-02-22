<<<<<<< HEAD
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

> NOTE: The `.envs` folder only has `.envs/.local` settings, these are project wide local **sandbox only account** settings. If you need your own local settings use a .env file in the root of your project to override/set env variables (this _should_ be avoided). For example, I typically have a `NGROK_URL` that changes frequently to point to my local machine for 3rd party API callbacks during development, which I place in `.env`. Production settings (`.envs/.production`) can be supplied to those who need them to build the final containers.

## Development App
Out of the box, we have all this running already. **Now get to the actual work!**
### Browser sync
- `http://localhost:3000/` - app running under BrowserSync
- `http://localhost:3001` - BrowserSync GUI

### Runserver
- `http://localhost:8000/` - Django
- `http://localhost:8000/admin/` - Django Admin

### Docs
- `http://localhost:8989/` - MkDocs for the project
- `http://localhost:8000/api/v1/swagger/` - Swagger docs
- `http://localhost:8000/api/v1/redoc/` - Redoc docs

{% if cookiecutter.use_mailhog == "y" %}
### Email
- `http://localhost:8025/` - Mailhog (receives all emails sent from Django, no matter the to address)
{% endif %}

{% if cookiecutter.use_celery == "y" %}
### Celery / Flower
- `http://localhost:5555/` - Flower GUI
{% endif %}

## Contributing
Run `pre-commit install` and **DO NOT** change the `.pre-commit-config.yaml`. This ensure **all contributions** output the same formatted code. When attempting to commit, the pre-commit hooks will run and you can fix any issues found.
=======
# {{cookiecutter.project_name}}

{{ cookiecutter.description }}

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

{%- if cookiecutter.open_source_license != "Not open source" %}

License: {{cookiecutter.open_source_license}}
{%- endif %}

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy {{cookiecutter.project_slug}}

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

{%- if cookiecutter.use_celery == "y" %}

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd {{cookiecutter.project_slug}}
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

{%- endif %}
{%- if cookiecutter.use_mailhog == "y" %}

### Email Server

{%- if cookiecutter.use_docker == "y" %}

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`
{%- else %}

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use [MailHog](https://github.com/mailhog/MailHog) when generating the project a local SMTP server with a web interface will be available.

1.  [Download the latest MailHog release](https://github.com/mailhog/MailHog/releases) for your OS.

2.  Rename the build to `MailHog`.

3.  Copy the file to the project root.

4.  Make it executable:

        $ chmod +x MailHog

5.  Spin up another terminal window and start it there:

        ./MailHog

6.  Check out <http://127.0.0.1:8025/> to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

{%- endif %}

{%- endif %}
{%- if cookiecutter.use_sentry == "y" %}

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.
{%- endif %}

## Deployment

The following details how to deploy this application.
{%- if cookiecutter.use_heroku.lower() == "y" %}

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

{%- endif %}
{%- if cookiecutter.use_docker.lower() == "y" %}

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

{%- endif %}
{%- if cookiecutter.custom_bootstrap_compilation == "y" %}
### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

{%- if cookiecutter.js_task_runner == "Gulp" %}
Bootstrap's javascript as well as its dependencies is concatenated into a single file: `static/js/vendors.js`.
{%- endif %}

{%- endif %}
>>>>>>> upstream/master
