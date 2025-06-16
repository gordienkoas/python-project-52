install:
	uv sync

#lint:
#	ruff check .
#
migrate:
	uv run python manage.py migrate
#
#collectstatic:
#	uv run python manage.py collectstatic

build:
	./build.sh

#test:
#	pytest

render-start:
	gunicorn task_manager.wsgi:application

