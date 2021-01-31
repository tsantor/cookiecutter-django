superuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

migrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate
