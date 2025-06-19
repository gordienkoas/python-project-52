install:
	uv sync

build:
	./build.sh

lint:
	ruff check .

#migrate:
#	uv run python manage.py migrate

start:
	cd code && ../.venv/bin/python manage.py runserver 0.0.0.0:8000

test:
	pytest

render-start:
	gunicorn task_manager.wsgi:application

