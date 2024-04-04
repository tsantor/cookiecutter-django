# {{cookiecutter.project_name}}

{{ cookiecutter.description }}

### Clone the Repo

```bash
git clone https://bitbucket.org/xstudios/{{ cookiecutter.project_slug }}
```

## Basic Commands
Run `make` to view a list of available commands.


## Create a Development Environment using Docker

```bash
make up
```

> NOTE: The `.envs` folder only has `.envs/.local` settings, these are project wide local **sandbox only account** settings. If you need your own local settings use a .env file in the root of your project to override/set env variables (this _should_ be avoided). Production settings (`.envs/.production`) will be supplied to those who need them to build the final images.


### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```bash
$ make pytest
$ make coverage
$ open open_coverage
```

## Development

Out of the box, we have all this running already. **Now get to the actual work!**

### Browser sync

- `http://localhost:3000/` - app running under BrowserSync
- `http://localhost:3001` - BrowserSync GUI

### Runserver

- `http://localhost:8000/` - Django
- `http://localhost:8000/admin/` - Django Admin

### Docs

- `http://localhost:8989/` - MkDocs for the project (recommend you move this to a dedicated repo)
- `http://localhost:8000/api/v1/swagger/` - Swagger docs
- `http://localhost:8000/api/v1/redoc/` - Redoc docs

### Email

- `http://localhost:8025/` - Mailpit (receives all emails sent from Django, no matter the to address)

### Celery / Flower

- `http://localhost:5555/` - Flower GUI

## Production

Create the following DNS records:

- {{ cookiecutter.domain_name }}
- traefik.{{ cookiecutter.domain_name }}
{%- if cookiecutter.use_celery == 'y' %}
- flower.{{ cookiecutter.domain_name }}
{%- endif %}
{%- if cookiecutter.use_prometheus == 'y' %}
- prometheus.{{ cookiecutter.domain_name }}
{%- endif %}
{%- if cookiecutter.use_grafana == 'y' %}
- grafana.{{ cookiecutter.domain_name }}
{%- endif %}

Run commands:

- On local machine run, `make rsync_to_prod` (ensure production envs exist!)
- On production, run `make nginx_htaccess`
- On production, run `make traefik_htaccess`
- On production, run `make deploy_prod`

### Dashboards
 - https://traefik.{{ cookiecutter.domain_name }}/dashboard
{%- if cookiecutter.use_celery == 'y' %}
 - https://flower.{{ cookiecutter.domain_name }}
{%- endif %}
{%- if cookiecutter.use_prometheus == 'y' %}
 - https://prometheus.{{ cookiecutter.domain_name }}
{%- endif %}
{%- if cookiecutter.use_grafana == 'y' %}
 - https://grafana.{{ cookiecutter.domain_name }}
{%- endif %}

## Security
Run a port scan and ensure the ports you need open are open. Typically only 80 and 443 as Traefik will proxy to appropriate service ports.

```
nmap -p 80,443,1883,8883,9001,5432,5555,3000,9090 {{ cookiecutter.domain_name }}
```

## Contributing

Run `pre-commit install` and **DO NOT** change the `.pre-commit-config.yaml`. This ensure **all contributions** output the same formatted code. When attempting to commit, the pre-commit hooks will run and you **must** fix any issues found.
