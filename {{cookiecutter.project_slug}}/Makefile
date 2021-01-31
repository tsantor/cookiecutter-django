superuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

migrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate

dev_up:
	docker-compose -f local.yml up --remove-orphans

dev_down:
	docker-compose -f local.yml down
