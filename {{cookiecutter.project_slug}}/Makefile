# I like to think of a Makefile as a "make my life easier" file, less typing

python_version=3.9.4
venv={{cookiecutter.project_slug}}_env

user={{cookiecutter.project_user}}
project_dir={{cookiecutter.project_slug}}

local=docker-compose -f local.yml
staging_ssh=${user}@staging.{{cookiecutter.domain_name}}

prod=docker-compose -f production.yml
prod_ssh=${user}@{{cookiecutter.domain_name}}
ssh_key=""

aws_profile=default
s3_bucket=bucketname

# -----------------------------------------------------------------------------
# Local
# -----------------------------------------------------------------------------

env:
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

reqs:
	python -m pip install -U pip black pylint pre-commit && pre-commit install

build_django:
	${local} build django
	${local} build celeryworker
	${local} build celerybeat

restart_django:
	${local} restart django
	${local} restart celeryworker
	${local} restart celerybeat

pip_list:
	${local} run --rm django python -m pip list

up:
	${local} up --remove-orphans

down:
	${local} down

superuser:
	${local} run --rm django python manage.py createsuperuser

migrations:
	${local} run --rm django python manage.py makemigrations

migrate:
	${local} run --rm django python manage.py migrate

show_urls:
	${local} run --rm django python manage.py show_urls

shell:
	${local} run --rm django python manage.py shell_plus

clearsessions:
	${local} run --rm django python manage.py clearsessions

pull_live_db:
	rsync -avzP ${prod_ssh}:~/production_db.dump .

pull_media:
	aws s3 sync --profile=${aws_profile} s3://${s3_bucket}/media ./media/ \
		--exclude "*.DS_Store"

push_staging_env:
	rsync -avzP .envs/.staging ${staging_ssh}:~/${project_dir}/.envs/

pull_staging_env:
	rsync -avzP ${staging_ssh}:~/${project_dir}/.envs/.staging .envs/

# Project Specific


# -----------------------------------------------------------------------------
# Production only
# -----------------------------------------------------------------------------

prod_up:
	${prod} up -d --remove-orphans

prod_down:
	${prod} down

prod_migrate:
	${prod} run --rm django python manage.py migrate

prod_collectstatic:
	${prod} run --rm django python manage.py collectstatic --noinput

prod_build_django:
	${prod} build django
	${prod} build celeryworker
	${prod} build celerybeat

prod_restart_django:
	${prod} restart django
	${prod} restart celeryworker
	${prod} restart celerybeat

push_production_env:
	rsync -avzP ${ssh_key} .envs/.production ${prod_ssh}:~/${project_dir}/.envs/

pull_production_env:
	rsync -avzP ${ssh_key} ${prod_ssh}:~/${project_dir}/.envs/.production .envs/

# Project Specific
