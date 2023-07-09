.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# -----------------------------------------------------------------------------

python_version=3.9.11
venv={{cookiecutter.project_slug}}_env

user={{cookiecutter.project_user}}
project_dir={{cookiecutter.project_slug}}

prod_ssh=${user}@{{cookiecutter.domain_name}}

aws_profile=default
s3_bucket=bucketname

# -----------------------------------------------------------------------------
# Local
# -----------------------------------------------------------------------------

env:  ## create virtualenv
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

reqs:  ## install bare minimum dev reqs
	python3 -m pip install -U pip wheel
	python3 -m pip install pre-commit install

reqs_local:  ## install local dev reqs
	python3 -m pip install -r requirements/local.txt

build:  ## build docker containers
	docker-compose -f local.yml build

up:  ## run docker containers
	docker-compose -f local.yml up --remove-orphans

down:  ## stop docker containers
	docker-compose -f local.yml down

pip_list:  ## run pip list
	docker-compose -f local.yml exec django python3 -m pip list

pip_freeze:  ## run pipfreezer
	docker-compose -f local.yml exec django pipfreezer

superuser:  ## create a django superuser
	docker-compose -f local.yml exec django python manage.py createsuperuser

migrations:  ## create django migrations
	docker-compose -f local.yml run --rm django python manage.py makemigrations

migrate:  ## run django migrations
	docker-compose -f local.yml exec django python manage.py migrate

show_urls:  ## show urls
	docker-compose -f local.yml exec django python manage.py show_urls

shell:  ## run shell
	docker-compose -f local.yml exec django python manage.py shell_plus

clearsessions:  ## clear django sessions
	docker-compose -f local.yml exec django python manage.py clearsessions

collectstatic:  ## collect static files
	docker-compose -f local.yml exec django python manage.py collectstatic

pytest:  ## run pytest
	docker-compose -f local.yml exec django pytest -v

pytest_verbose:  ## run pytest verbose mode
	docker-compose -f local.yml exec django pytest -vs

optimize:  ## optimize images
	find . -name '*.png' -exec pngquant 64 --ext .png -f --skip-if-larger {} \;
	cd {{cookiecutter.project_slug}}/static && open -a ImageOptim .

# -----------------------------------------------------------------------------
# Project Specific
# -----------------------------------------------------------------------------

clean_vue:
	rm -rf {{cookiecutter.project_slug}}/static/vue-frontend/

push_vue:
	rsync -avzP face_amusement/static/vue-frontend ${prod_ssh}:~/${project_dir}/{{cookiecutter.project_slug}}/static

fake_gameplay:
	docker-compose -f local.yml exec django python manage.py fake_gameplay

test_core:
	docker-compose -f local.yml exec django pytest -v {{cookiecutter.project_slug}}/core

test_verbose:
	docker-compose -f local.yml exec django pytest -vs {{cookiecutter.project_slug}}/core

# -----------------------------------------------------------------------------
# Local - Use caution!
# -----------------------------------------------------------------------------

pull_media:  ## pull media from s3
	aws s3 sync --profile=${aws_profile} s3://${s3_bucket}/media ./media/ \
		--exclude "*.DS_Store"

push_production_env:  ## push production env file
	rsync -avzP .envs/.production ${prod_ssh}:~/${project_dir}/.envs/
	# rsync -avzP -e "ssh -i ~/.ssh/{{cookiecutter.project_slug}}.pem" .envs/.production ${prod_ssh}:${project_dir}/.envs/

pull_production_env:  ## pull production env file
	rsync -avzP ${prod_ssh}:~/${project_dir}/.envs/.production .envs/
	# rsync -avzP -e "ssh -i ~/.ssh/{{cookiecutter.project_slug}}.pem" ${prod_ssh}:~/${project_dir}/.envs/.production .envs/

dump_data:  ## dumb data to a fixture
	docker-compose -f local.yml exec django python manage.py dumpdata \
  --natural-foreign --natural-primary \
  -e contenttypes \
  -e sessions  \
  -e admin \
  -e django_celery_results.taskresult \
  -e oauth2_provider.accesstoken \
  -e oauth2_provider.refreshtoken \
  -e oauth2_provider.grant \
  -e oauth2_provider.idtoken > ${project_dir}/fixtures/data.json

load_data:  ## load data from a fixture
	docker-compose -f local.yml run --rm django python manage.py loaddata data.json

# -----------------------------------------------------------------------------
# Prod
# -----------------------------------------------------------------------------

deploy_prod:  ## lazy deploy on prod (down, build, migrate, up)
	docker-compose -f production.yml down
	docker-compose -f production.yml build
	docker-compose -f production.yml run --rm django python manage.py migrate
	docker-compose -f production.yml up -d

# -----------------------------------------------------------------------------
# Mutagen
# -----------------------------------------------------------------------------

mutagen_sync_name={{cookiecutter.project_slug}}-code
mutagen_forward_name={{cookiecutter.project_slug}}-port-forward
mutagen_beta_user=tsantor@tim-macbook-ubuntu.local
mutagen_beta_dir=~/Projects/{{cookiecutter.project_slug}}

mutagen_up:  ## mutagen create
	mutagen sync create --name=${mutagen_sync_name} . ${mutagen_beta_user}:${mutagen_beta_dir}
	mutagen forward create --name=${mutagen_forward_name}p tcp:localhost:8000 ${mutagen_beta_user}:22:tcp::8000
	mutagen forward create --name=${mutagen_forward_name} tcp:localhost:5432 ${mutagen_beta_user}:22:tcp::5432

mutagen_pause:  ## mutagen pause
	mutagen sync pause ${mutagen_sync_name}
	mutagen forward pause ${mutagen_forward_name}

mutagen_resume:  ## mutagen resume
	mutagen sync resume ${mutagen_sync_name}
	mutagen forward resume ${mutagen_forward_name}

mutagen_down:  ## mutagen terminate
	mutagen sync terminate ${mutagen_sync_name}
	mutagen forward terminate ${mutagen_forward_name}
