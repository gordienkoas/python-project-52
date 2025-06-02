install:
	uv sync

migrate:
	python manage.py migrate

build:
	./build.sh

render-start:
	python -m gunicorn task_manager.wsgi:application
