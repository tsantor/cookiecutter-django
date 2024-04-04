# -----------------------------------------------------------------------------
# Generate help output when running just `make`
# -----------------------------------------------------------------------------
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
# Project specific variables
# -----------------------------------------------------------------------------

python_version=3.9.11
venv={{cookiecutter.project_slug}}_env

user={{cookiecutter.project_user}}
project_dir={{cookiecutter.project_slug}}
project_package={{cookiecutter.project_slug}} # typically we use underscored version of project_slug
app={{cookiecutter.project_slug}}

staging_ssh=${user}@staging.{{cookiecutter.domain_name}}
prod_ssh=${user}@{{cookiecutter.domain_name}}

aws_profile=default
s3_bucket=bucketname

mutagen_sync_name={{cookiecutter.project_slug}}-code
mutagen_forward_name={{cookiecutter.project_slug}}-port-forward
mutagen_beta_user=tsantor@tim-macbook-ubuntu.local
mutagen_beta_dir=~/Projects/{{cookiecutter.project_slug}}

local_compose=docker-compose -f local.yml
staging_compose=docker-compose -f staging.yml
prod_compose=docker-compose -f production.yml

# START - Generic commands
# -----------------------------------------------------------------------------
# Environment
# -----------------------------------------------------------------------------

env: ## create virtualenv
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

env_remove:  ## remove virtual environment
	pyenv uninstall ${venv}

# -----------------------------------------------------------------------------
# Pip
# -----------------------------------------------------------------------------

pip_install: ## install requirements
	python3 -m pip install -U pip wheel build pre-commit && pre-commit install

pip_list:  ## run pip list
	${local_compose} exec django python -m pip list

pip_freeze:  ## run pipfreezer
	${local_compose} exec django pipfreezer

pip_checker:  ## run pipchecker
	${local_compose} exec django pipchecker

# -----------------------------------------------------------------------------
# Docker
# -----------------------------------------------------------------------------

build:  ## build docker containers
	${local_compose} build

up:  ## run docker containers
	${local_compose} up --remove-orphans

down:  ## stop docker containers
	${local_compose} down

build_django:  ## build django
	${local_compose} build django
	${local_compose} build celeryworker
	${local_compose} build celerybeat

bash_django: ## run bash in django container
	${local_compose} exec django bash

view_env:  ## view environment variables
	${local_compose} run --rm django env | sort

# -----------------------------------------------------------------------------
# Django
# -----------------------------------------------------------------------------

manage:	## run django manage.py (eg - make manage cmd="shell")
	${local_compose} exec django python manage.py ${cmd}

superuser:  ## create a django superuser
	${local_compose} exec django python manage.py createsuperuser

migrations:  ## create django migrations (eg - make migrations app="core")
	${local_compose} exec django python manage.py makemigrations ${app}

migrate:  ## run django migrations
	${local_compose} exec django python manage.py migrate

show_urls:  ## show urls
	${local_compose} exec django python manage.py show_urls

shell:  ## run shell plus
	${local_compose} exec django python manage.py shell_plus

clearsessions:  ## clear django sessions
	${local_compose} exec django python manage.py clearsessions

collectstatic:  ## collect static files
	${local_compose} exec django python manage.py collectstatic

cleartokens:  ## clear tokens
	${local_compose} exec django python manage.py cleartokens

flush: ## flush db
	${local_compose} exec django python manage.py flush

remove_stale_contenttypes:  ## remove stale contenttypes
	${local_compose} exec django python manage.py remove_stale_contenttypes --include-stale-apps

# start_app:	## start a new app
# 	${local_compose} exec django python manage.py startapp ${app_name} --template

dump_basic_data:  ## dump basic data to a fixture
	mkdir -p ${project_dir}/fixtures
	${local_compose} exec django python manage.py dumpdata \
	--natural-foreign --natural-primary \
	-e admin \
	-e contenttypes \
	-e sessions  \
	-e django_celery_beat \
	> ${project_dir}/fixtures/basic_data.json

load_basic_data:  ## load basic data from a fixture
	${local_compose} run --rm django python manage.py loaddata basic_data.json

drop_db: ## drop db
	${local_compose} run --rm django python manage.py drop_database

# -----------------------------------------------------------------------------
# Testing
# -----------------------------------------------------------------------------

pytest:  ## run pytest
	${local_compose} exec django pytest ${app}

pytest_verbose:  ## runs pytest with verbose output
	${local_compose} exec django pytest -vs ${app}

coverage:  ## run coverage
	${local_compose} exec django bash -c "coverage run -m pytest -v ${app} && coverage html"

coverage_skip:  ## run coverage (skip-comvered)
	${local_compose} exec django bash -c "coverage run -m pytest ${app} && coverage html --skip-covered"

open_coverage:  ## open coverage report
	open htmlcov/index.html

drop_test_db:  ## drop test db
	${local_compose} exec django python manage.py drop_test_database

test:  ## run tests
	${local_compose} exec django python manage.py test

mypy:	## run mypy
	${local_compose} exec django mypy ${app}

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------

clean_build: ## remove build artifacts
	rm -fr build/ dist/ .eggs/
	find . -name '*.egg-info' -o -name '*.egg' -exec rm -fr {} +

clean_pyc: ## remove python file artifacts
	find . \( -name '*.pyc' -o -name '*.pyo' -o -name '*~' -o -name '__pycache__' \) -exec rm -fr {} +

clean: clean_build clean_pyc ## remove all build and python artifacts

clean_pytest_cache:  ## clear pytest cache
	rm -rf .pytest_cache

clean_tox_cache:  ## clear tox cache
	rm -rf .tox

clean_coverage:  ## clear coverage cache
	rm .coverage
	rm -rf htmlcov

clean_tests: clean_pytest_cache clean_tox_cache clean_coverage  ## clear pytest, tox, and coverage caches

# -----------------------------------------------------------------------------
# Gen password files
# -----------------------------------------------------------------------------

traefik_htaccess:  ## create .htpasswd file
	# sudo apt install apache2-utils
	htpasswd -c compose/production/traefik/.htpasswd ${user}
	# ${prod_compose} build --no-cache traefik

nginx_htaccess:  ## create .htpasswd file
	# sudo apt install apache2-utils
	htpasswd -c compose/production/nginx/.htpasswd ${user}
	# ${prod_compose} build --no-cache nginx

# -----------------------------------------------------------------------------
# Vue SPA Specific
# -----------------------------------------------------------------------------

clean_vue:  ## clean vue directory
	rm -rf ${project_package}/static/vue-frontend/

push_vue: ## rsync vue-frontend to serverr
	rsync -avzP ${project_package}/static/vue-frontend ${prod_ssh}:~/${project_dir}/${project_package}/static

# -----------------------------------------------------------------------------
# Staging only
# -----------------------------------------------------------------------------

staging_pull_db:  ## pull staging db
	# rsync -avzP -e "ssh -i ~/.ssh/findershare.pem" ${staging_ssh}:~/staging_db.dump .
	rsync -avzP ${staging_ssh}:~/staging_db.dump .

staging_push_env:  ## push staging env
	rsync -avzP .envs/.staging ${staging_ssh}:${project_dir}/.envs/

staging_pull_env:  ## pull staging env
	rsync -avzP ${staging_ssh}:${project_dir}/.envs/.staging .envs/

staging_deploy:  ## deploy on staging
	${staging_compose} down
	${staging_compose} build
	${staging_compose} run --rm django python manage.py migrate
	${staging_compose} up -d

# -----------------------------------------------------------------------------
# Production only
# -----------------------------------------------------------------------------

prod_up:  ## run docker containers
	${prod_compose} up -d --remove-orphans

prod_down:  ## stop docker containers
	${prod_compose} down

prod_migrate:  ## run django migrations
	${prod_compose} run --rm django python manage.py migrate

prod_collectstatic:  ## collect static files
	${prod_compose} run --rm django python manage.py collectstatic --noinput

prod_manage:	## run django manage.py (eg - make manage cmd="shell")
	${prod_compose} exec django python manage.py ${cmd}

prod_rebuild_django:  ## rebuild django
	${prod_compose} stop django
	${prod_compose} build --no-cache django
	${prod_compose} up -d django

	${prod_compose} stop celeryworker >/dev/null 2>&1
	${prod_compose} up -d celeryworker >/dev/null 2>&1

	${prod_compose} stop celerybeat >/dev/null 2>&1
	${prod_compose} up -d celerybeat >/dev/null 2>&1

prod_rebuild_nginx:  ## rebuild nginx
	${prod_compose} stop nginx
	${prod_compose} build --no-cache nginx
	${prod_compose} up -d nginx

prod_rebuild_traefik:  ## rebuild traefik
	${prod_compose} stop traefik
	${prod_compose} build --no-cache traefik
	${prod_compose} up -d traefik

prod_rebuild_prometheus:  ## rebuild prometheus
	${prod_compose} stop prometheus
	${prod_compose} build --no-cache prometheus
	${prod_compose} up -d prometheus

prod_rebuild_grafana:  ## rebuild grafana
	${prod_compose} stop grafana
	${prod_compose} build --no-cache grafana
	${prod_compose} up -d grafana

prod_pull_db:  ## pull live db
	# rsync -avzP -e "ssh -i ~/.ssh/findershare.pem" ${prod_ssh}:~/production_db.dump .
	rsync -avzP ${prod_ssh}:~/production_db.dump .

prod_push_env:  ## push production env
	rsync -avzP .envs/.production ${prod_ssh}:${project_dir}/.envs/

prod_pull_env: ## pull production env
	rsync -avzP -e "ssh -i ~/.ssh/findershare.pem" ${prod_ssh}:${project_dir}/.envs/.production .envs/

prod_deploy:  ## deploy on production
	${prod_compose} down
	${prod_compose} build
	${prod_compose} run --rm django python manage.py migrate
	${prod_compose} up -d

prod_deploy_no_cache:  ## deploy on production (no cache)
	${prod_compose} down
	${prod_compose} build --no-cache
	${prod_compose} run --rm django python manage.py migrate
	${prod_compose} up -d

prod_env:  ## view environment variables
	${prod_compose} run --rm django env | sort

prod_uptime:	## view uptime
	{% raw %} docker ps --format "table {{.Names}}\t{{.Status}}"{% endraw %}

# -----------------------------------------------------------------------------
# Optimization
# -----------------------------------------------------------------------------

optimize_pngs:  ## optimize PNGs
	find . -name '*.png' -exec pngquant 64 --ext .png -f --skip-if-larger {} \;

optimize_jpgs:  ## optimize JPGs
	cd ${project_dir}/static && open -a ImageOptim .

count_lines:  ## count lines of code
	# Includes blank lines and comments
	# find . -name '*.py' ! -path '*/migrations/*' ! -path '*/config/settings/*' | xargs wc -l
	# No blank lines or comments
	find . -name '*.py' ! -path '*/migrations/*' \
		! -path '*/config/settings/*' \
		-exec grep -vE '^\s*($$|#)' {} \; | wc -l | tr -d ' '

# -----------------------------------------------------------------------------
# Miscellaneous
# -----------------------------------------------------------------------------

tree:  ## Show directory tree
	tree -I 'build|dist|htmlcov|node_modules|migrations|contrib|__pycache__|*.egg-info'

# -----------------------------------------------------------------------------
# Mutagen
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Experimental (Use caution!)
# -----------------------------------------------------------------------------

pull_media:  ## pull media from s3
	aws s3 sync --profile=${aws_profile} s3://${s3_bucket}/media ./media/ \
		--exclude "*.DS_Store" --exclude cache/ --exclude "*.mp4"

rsync_to_prod:  ## rsync to prod (for down n' dirty testing)
	# -e "ssh -i ~/.ssh/your-key.pem"
	rsync -avzP . ${prod_ssh}:~/${project_dir}/ \
		--exclude ".coverage" \
		--exclude ".DS_Store" \
		--exclude ".editorconfig" \
		--exclude ".env" \
		--exclude ".envs/.local" \
		--exclude ".git" \
		--exclude ".ipython" \
		--exclude ".pytest_cache" \
		--exclude ".vscode" \
		--exclude "htmlcov" \
		--exclude "media/" \
		--exclude "node_modules" \
		--exclude "staticfiles/" \
		--exclude "**/.htpasswd"

# END - Generic commands
# -----------------------------------------------------------------------------
# Project Specific
# -----------------------------------------------------------------------------

# Add your project specific commands here
