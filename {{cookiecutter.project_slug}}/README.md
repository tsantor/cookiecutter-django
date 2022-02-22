# {{ cookiecutter.project_name }}

## Tech Stack

- Ubuntu 20.04 LTS
- Django 3
- Python 3.8
- Nginx
- Gunicorn
- PostgreSQL
- Redis
- Celery


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
