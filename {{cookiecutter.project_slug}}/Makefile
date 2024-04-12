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
project_package={{cookiecutter.project_slug}}

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

env:  ## Create virtual environment (uses `pyenv`)
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

env_remove:  ## Remove virtual environment
	pyenv uninstall -f ${venv}

env_from_scratch: env_remove env pip_install  ## Create environment from scratch

# -----------------------------------------------------------------------------
# Pip
# -----------------------------------------------------------------------------

pip_install:  ## Install requirements
	python3 -m pip install -U pip wheel build ruff pre-commit && pre-commit install

pip_list:  ## Run pip list
	${local_compose} exec django python -m pip list

pip_freeze:  ## Run pipfreezer
	${local_compose} exec django pipfreezer

pip_checker:  ## Run pipchecker
	${local_compose} exec django pipchecker

# -----------------------------------------------------------------------------
# Docker
# -----------------------------------------------------------------------------

build:  ## Build docker containers
	${local_compose} build

up:  ## Run docker containers
	${local_compose} up --remove-orphans

down:  ## Stop docker containers
	${local_compose} down

build_django:  ## Build django
	${local_compose} build django
	${local_compose} build celeryworker
	${local_compose} build celerybeat

bash_django:  ## Run bash in django container
	${local_compose} exec django bash

view_env:  ## View environment variables
	${local_compose} run --rm django env | sort

# -----------------------------------------------------------------------------
# Django
# -----------------------------------------------------------------------------

manage:	## Run django manage.py (eg - `make manage cmd="shell"`)
	${local_compose} exec django python manage.py ${cmd}

superuser:  ## Create a django superuser
	${local_compose} exec django python manage.py createsuperuser

migrations:  ## Create django migrations (eg - `make migrations app="core"`)
	${local_compose} exec django python manage.py makemigrations ${app}

migrate:  ## Run django migrations
	${local_compose} exec django python manage.py migrate

show_urls:  ## Show urls
	${local_compose} exec django python manage.py show_urls

shell:  ## Run shell plus
	${local_compose} exec django python manage.py shell_plus

clearsessions:  ## Clear django sessions
	${local_compose} exec django python manage.py clearsessions

collectstatic:  ## Collect static files
	${local_compose} exec django python manage.py collectstatic

cleartokens:  ## Clear tokens
	${local_compose} exec django python manage.py cleartokens

flush:  ## Flush db
	${local_compose} exec django python manage.py flush

remove_stale_contenttypes:  ## Remove stale contenttypes
	${local_compose} exec django python manage.py remove_stale_contenttypes --include-stale-apps

start_app:	## Start a new app (uses github.com/tsantor/django-startapp-template)
	${local_compose} exec django python manage.py startapp \
		--template=https://github.com/tsantor/django-startapp-template/archive/master.zip \
		${name}
	rm ${name}/.gitignore
	rm ${name}/README.md

dump_basic_data:  ## Dump basic data to a fixture
	mkdir -p ${project_dir}/fixtures
	${local_compose} exec django python manage.py dumpdata \
	--natural-foreign --natural-primary \
	-e admin \
	-e contenttypes \
	-e sessions  \
	-e django_celery_beat \
	> ${project_dir}/fixtures/basic_data.json

load_basic_data:  ## Load basic data from a fixture
	${local_compose} run --rm django python manage.py loaddata basic_data.json

drop_db:  ## Drop db
	${local_compose} run --rm django python manage.py drop_database

# -----------------------------------------------------------------------------
# Testing
# -----------------------------------------------------------------------------

pytest:  ## Run pytest
	${local_compose} exec django pytest -vx ${project_dir}

pytest_verbose:  ## Runs pytest with verbose output
	${local_compose} exec django pytest -vvs ${project_dir}

coverage:  ## Run coverage
	${local_compose} exec django bash -c "coverage run -m pytest ${project_dir} && coverage html"

coverage_skip:  ## Run coverage (skip-covered)
	${local_compose} exec django bash -c "coverage run -m pytest ${project_dir} && coverage html --skip-covered"

open_coverage:  ## Open coverage report
	open htmlcov/index.html

drop_test_db:  ## Drop test db
	${local_compose} exec django python manage.py drop_test_database

test:  ## Run tests
	${local_compose} exec django python manage.py test

mypy:	 ## Run mypy
	${local_compose} exec django mypy ${project_dir}

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------

clean_build:  ## Remove build artifacts
	rm -fr build/ dist/ .eggs/
	find . -name '*.egg-info' -o -name '*.egg' -exec rm -fr {} +

clean_pyc:  ## Remove python file artifacts
	find . \( -name '*.pyc' -o -name '*.pyo' -o -name '*~' -o -name '__pycache__' \) -exec rm -fr {} +

clean: clean_build clean_pyc ## Remove all build and python artifacts

clean_pytest_cache:  ## Clear pytest cache
	rm -rf .pytest_cache

clean_ruff_cache:  ## Clear ruff cache
	rm -rf .ruff_cache

clean_tox_cache:  ## Clear tox cache
	rm -rf .tox

clean_coverage:  ## Clear coverage cache
	rm .coverage
	rm -rf htmlcov

clean_tests: clean_pytest_cache clean_ruff_cache clean_tox_cache clean_coverage  ## Clear pytest, ruff, tox, and coverage caches

# -----------------------------------------------------------------------------
# Generate Passwords
# -----------------------------------------------------------------------------

traefik_htaccess:  ## Create .htpasswd file
	# sudo apt install apache2-utils
	htpasswd -c compose/production/traefik/.htpasswd ${user}
	# ${prod_compose} build --no-cache traefik

nginx_htaccess:  ## Create .htpasswd file
	# sudo apt install apache2-utils
	htpasswd -c compose/production/nginx/.htpasswd ${user}
	# ${prod_compose} build --no-cache nginx

# -----------------------------------------------------------------------------
# Vue SPA Specific
# -----------------------------------------------------------------------------

clean_vue:  ## Clean vue directory
	rm -rf ${project_package}/static/vue-frontend/

push_vue:  ## Rsync vue-frontend to serverr
	rsync -avzP ${project_package}/static/vue-frontend ${prod_ssh}:~/${project_dir}/${project_package}/static

# -----------------------------------------------------------------------------
# Staging
# -----------------------------------------------------------------------------

staging_pull_db:  ## Pull staging db
	# rsync -avzP -e "ssh -i ~/.ssh/findershare.pem" ${staging_ssh}:~/staging_db.dump .
	rsync -avzP ${staging_ssh}:~/staging_db.dump .

staging_push_env:  ## Push staging env
	rsync -avzP .envs/.staging ${staging_ssh}:${project_dir}/.envs/

staging_pull_env:  ## Pull staging env
	rsync -avzP ${staging_ssh}:${project_dir}/.envs/.staging .envs/

staging_deploy:  ## Deploy on staging
	${staging_compose} down
	${staging_compose} build
	${staging_compose} run --rm django python manage.py migrate
	${staging_compose} up -d

# -----------------------------------------------------------------------------
# Production
# -----------------------------------------------------------------------------

prod_up:  ## Run docker containers
	${prod_compose} up -d --remove-orphans

prod_down:  ## Stop docker containers
	${prod_compose} down

prod_migrate:  ## Run django migrations
	${prod_compose} run --rm django python manage.py migrate

prod_collectstatic:  ## Collect static files
	${prod_compose} run --rm django python manage.py collectstatic --noinput

prod_manage:	## Run django manage.py (eg - `make manage cmd="shell"`)
	${prod_compose} exec django python manage.py ${cmd}

prod_superuser:  ## Create a django superuser
	${prod_compose} exec django python manage.py createsuperuser

prod_rebuild_django:  ## Rebuild django
	${prod_compose} stop django
	${prod_compose} build --no-cache django
	${prod_compose} up -d django

	${prod_compose} stop celeryworker >/dev/null 2>&1
	${prod_compose} up -d celeryworker >/dev/null 2>&1

	${prod_compose} stop celerybeat >/dev/null 2>&1
	${prod_compose} up -d celerybeat >/dev/null 2>&1

prod_rebuild_nginx:  ## Rebuild nginx
	${prod_compose} stop nginx
	${prod_compose} build --no-cache nginx
	${prod_compose} up -d nginx

prod_rebuild_traefik:  ## Rebuild traefik
	${prod_compose} stop traefik
	${prod_compose} build --no-cache traefik
	${prod_compose} up -d traefik

prod_rebuild_prometheus:  ## Rebuild prometheus
	${prod_compose} stop prometheus
	${prod_compose} build --no-cache prometheus
	${prod_compose} up -d prometheus

prod_rebuild_grafana:  ## Rebuild grafana
	${prod_compose} stop grafana
	${prod_compose} build --no-cache grafana
	${prod_compose} up -d grafana

prod_pull_db:  ## Pull live db
	# # -e "ssh -i ~/.ssh/your-key.pem"
	rsync -avzP ${prod_ssh}:~/production_db.dump .

prod_push_env:  ## Push production env
	rsync -avzP .envs/.production ${prod_ssh}:${project_dir}/.envs/

prod_pull_env:  ## Pull production env
	# -e "ssh -i ~/.ssh/your-key.pem"
	rsync -avzP ${prod_ssh}:${project_dir}/.envs/.production .envs/

prod_deploy:  ## Deploy on production
	${prod_compose} down
	${prod_compose} build
	${prod_compose} run --rm django python manage.py migrate
	${prod_compose} up -d

prod_deploy_no_cache:  ## Deploy on production (no cache)
	${prod_compose} down
	${prod_compose} build --no-cache
	${prod_compose} run --rm django python manage.py migrate
	${prod_compose} up -d

prod_env:  ## View environment variables
	${prod_compose} run --rm django env | sort

prod_uptime:	## View uptime
	{% raw %} docker ps --format "table {{.Names}}\t{{.Status}}"{% endraw %}

# -----------------------------------------------------------------------------
# Optimization
# -----------------------------------------------------------------------------

optimize_pngs:  ## Optimize PNGs
	find . -name '*.png' -exec pngquant 64 --ext .png -f --skip-if-larger {} \;

optimize_jpgs:  ## Optimize JPGs
	cd ${project_dir}/static && open -a ImageOptim .

count_lines:  ## Count lines of code
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

mutagen_up:  ## Mutagen create
	mutagen sync create --name=${mutagen_sync_name} . ${mutagen_beta_user}:${mutagen_beta_dir}
	mutagen forward create --name=${mutagen_forward_name}p tcp:localhost:8000 ${mutagen_beta_user}:22:tcp::8000
	mutagen forward create --name=${mutagen_forward_name} tcp:localhost:5432 ${mutagen_beta_user}:22:tcp::5432

mutagen_pause:  ## Mutagen pause
	mutagen sync pause ${mutagen_sync_name}
	mutagen forward pause ${mutagen_forward_name}

mutagen_resume:  ## Mutagen resume
	mutagen sync resume ${mutagen_sync_name}
	mutagen forward resume ${mutagen_forward_name}

mutagen_down:  ## Mutagen terminate
	mutagen sync terminate ${mutagen_sync_name}
	mutagen forward terminate ${mutagen_forward_name}

# -----------------------------------------------------------------------------
# Experimental (Use caution!)
# -----------------------------------------------------------------------------

pull_media:  ## Pull media from s3
	aws s3 sync --profile=${aws_profile} s3://${s3_bucket}/media ./media/ \
		--exclude "*.DS_Store" --exclude cache/ --exclude "*.mp4"

rsync_to_prod:  ## Rsync to prod (for down n' dirty testing)
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
