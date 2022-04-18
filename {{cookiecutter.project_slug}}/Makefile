# I like to think of a Makefile as a "make my life easier" file, less typing

python_version=3.9.11
venv={{cookiecutter.project_slug}}_env

user={{cookiecutter.project_user}}
project_dir={{cookiecutter.project_slug}}

staging_ssh=${user}@staging.{{cookiecutter.domain_name}}
prod_ssh=${user}@{{cookiecutter.domain_name}}

aws_profile=default
s3_bucket=bucketname

# -----------------------------------------------------------------------------
# Local
# -----------------------------------------------------------------------------

env:
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

reqs:
	python -m pip install -U pip wheel black pylint pre-commit && pre-commit install

build:
	docker-compose -f local.yml build

up:
	docker-compose -f local.yml up --remove-orphans

down:
	docker-compose -f local.yml down

pip_list:
	docker exec -it django python -m pip list

pip_freeze:
	docker exec -it django pipfreezer

superuser:
	docker exec -it django python manage.py createsuperuser

migrations:
	docker exec -it django python manage.py makemigrations

migrate:
	docker exec -it django python manage.py migrate

show_urls:
	docker exec -it django python manage.py show_urls

shell:
	docker exec -it django python manage.py shell_plus

clearsessions:
	docker exec -it django python manage.py clearsessions

collectstatic:
	docker exec -it django python manage.py collectstatic

# Project Specific
clean_vue:
	rm -rf {{cookiecutter.project_slug}}/static/vue-frontend/

push_vue:
	rsync -avzP ${ssh_key} {{cookiecutter.project_slug}}/static/vue-frontend ${prod_ssh}:~/${project_dir}/{{cookiecutter.project_slug}}/static

# -----------------------------------------------------------------------------
# Local - Use caution!
# -----------------------------------------------------------------------------

pull_live_db:
	rsync -avzP ${prod_ssh}:~/production_db.dump .

pull_media:
	aws s3 sync --profile=${aws_profile} s3://${s3_bucket}/media ./media/ \
		--exclude "*.DS_Store"

push_staging_env:
	rsync -avzP .envs/.staging ${staging_ssh}:~/${project_dir}/.envs/

push_production_env:
	rsync -avzP .envs/.production ${prod_ssh}:~/${project_dir}/.envs/

pull_staging_env:
	rsync -avzP ${staging_ssh}:~/${project_dir}/.envs/.staging .envs/

pull_production_env:
	rsync -avzP ${prod_ssh}:~/${project_dir}/.envs/.production .envs/


# Project Specific

# -----------------------------------------------------------------------------
# Prod
# -----------------------------------------------------------------------------

deploy_prod:
	docker-compose -f production up -d --build
	docker exec -it django python manage.py migrate
	docker exec -it django python manage.py collectstatic
