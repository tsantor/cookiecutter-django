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

Simply visit the following:

- [Public Website](http://localhost:8000/)
- [Django Admin](http://localhost:8000/)
- [MailPit](http://localhost:8025/)
- [Flower](http://localhost:5555/)
- [BrowserSync](http://localhost:3000/)
- [BrowserSync UI](http://localhost:3001/)

## Production Deploy
This is a simple deployment process to a **single** server.

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

Prep the server:
1. Create the `{{ cookiecutter.project_user }}` defined in your `Makefile` (do not use `root`)
1. SSH into your server as `{{ cookiecutter.project_user }}`
1. Run `sudo apt install make docker-compose apache2-utils`
1. Run:
    ```bash
    sudo groupadd docker
    sudo usermod -aG docker `{{ cookiecutter.project_user }}`
    newgrp docker
    ```

Run custom `make` commands:
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
