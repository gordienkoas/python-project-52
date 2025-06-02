install:
	uv sync

migrate:
	uv run python manage.py migrate

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi:application
