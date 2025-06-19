install:
	uv sync

build:
	./build.sh

lint:
	ruff check .

#migrate:
#	uv run python manage.py migrate

start:
	cd code && uv run manage.py runserver 0.0.0.0:3000

test:
	pytest

render-start:
	uv run gunicorn task_manager.wsgi:application

