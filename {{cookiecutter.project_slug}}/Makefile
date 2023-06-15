# I like to think of a Makefile as a "make my life easier" file, less typing

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

env:
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

reqs:
	python -m pip install -U pip wheel
	python -m pip install -r requirements/local.txt && pre-commit install

build:
	docker-compose -f local.yml build

up:
	docker-compose -f local.yml up --remove-orphans

down:
	docker-compose -f local.yml down

pip_list:
	docker-compose -f local.yml exec django python -m pip list

pip_freeze:
	docker-compose -f local.yml exec django pipfreezer

superuser:
	docker-compose -f local.yml exec django python manage.py createsuperuser

migrations:
	docker-compose -f local.yml exec django python manage.py makemigrations

migrate:
	docker-compose -f local.yml exec django python manage.py migrate

show_urls:
	docker-compose -f local.yml exec django python manage.py show_urls

shell:
	docker-compose -f local.yml exec django python manage.py shell_plus

clearsessions:
	docker-compose -f local.yml exec django python manage.py clearsessions

collectstatic:
	docker-compose -f local.yml exec django python manage.py collectstatic

pytest:
	docker-compose -f local.yml exec django pytest -v

# Project Specific
clean_vue:
	rm -rf {{cookiecutter.project_slug}}/static/vue-frontend/

push_vue:
	rsync -avzP {{cookiecutter.project_slug}}/static/vue-frontend ${prod_ssh}:~/${project_dir}/{{cookiecutter.project_slug}}/static

# -----------------------------------------------------------------------------
# Local - Use caution!
# -----------------------------------------------------------------------------

pull_live_db:
	rsync -avzP ${prod_ssh}:~/production_db.dump .

pull_media:
	aws s3 sync --profile=${aws_profile} s3://${s3_bucket}/media ./media/ \
		--exclude "*.DS_Store"

push_production_env:
	rsync -avzP .envs/.production ${prod_ssh}:~/${project_dir}/.envs/
	# rsync -avzP -e "ssh -i ~/.ssh/{{cookiecutter.project_slug}}.pem" .envs/.production ${prod_ssh}:${project_dir}/.envs/

pull_production_env:
	rsync -avzP ${prod_ssh}:~/${project_dir}/.envs/.production .envs/
	# rsync -avzP -e "ssh -i ~/.ssh/{{cookiecutter.project_slug}}.pem" ${prod_ssh}:~/${project_dir}/.envs/.production .envs/

dump_data:
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

load_data:
	docker-compose -f local.yml run --rm django python manage.py loaddata data.json

# Project Specific

# -----------------------------------------------------------------------------
# Prod
# -----------------------------------------------------------------------------

deploy_prod:
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

mutagen_up:
	mutagen sync create --name=${mutagen_sync_name} . ${mutagen_beta_user}:${mutagen_beta_dir}
	mutagen forward create --name=${mutagen_forward_name}p tcp:localhost:8000 ${mutagen_beta_user}:22:tcp::8000
	mutagen forward create --name=${mutagen_forward_name} tcp:localhost:5432 ${mutagen_beta_user}:22:tcp::5432

mutagen_pause:
	mutagen sync pause ${mutagen_sync_name}
	mutagen forward pause ${mutagen_forward_name}

mutagen_resume:
	mutagen sync resume ${mutagen_sync_name}
	mutagen forward resume ${mutagen_forward_name}

mutagen_down:
	mutagen sync terminate ${mutagen_sync_name}
	mutagen forward terminate ${mutagen_forward_name}
