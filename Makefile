install:
	uv sync

migrate:
	python manage.py migrate

build:
	./build.sh

render-start:
	venv/bin/gunicorn task_manager.wsgi:application
